from fastapi import FastAPI 
import os
from prometheus_fastapi_instrumentator import Instrumentator
from prometheus_client import Counter, Histogram, Gauge
import uvicorn
import time
from prometheus_client import REGISTRY

app = FastAPI() 
port = int(os.environ.get("PORT", 8005))

# Counter
if not any(metric.name == "demo_counter" for metric in REGISTRY.collect()):
    # Check if the metric already exists to avoid duplication
    demo_counter = Counter("demo_counter", "Total number of times /demo endpoint is called")
else:
    # If it exists, retrieve the existing metric
    demo_counter = Counter("demo_counter", "Total number of times /demo endpoint is called", registry= None)


# Histogram
if not any(metric.name == "demo_request_latency" for metric in REGISTRY.collect()):
    demo_latency_histogram = Histogram("demo_request_latency", "Latency for /demo endpoint requests",
                                    buckets=[0.1, 0.5, 1.0, 2.0, 5.0])
else:
    demo_latency_histogram = Histogram("demo_request_latency", "Latency for /demo endpoint requests",
                                    buckets=[0.1, 0.5, 1.0, 2.0, 5.0],registry=None)

# Gauge
if not any(metric.name == "active_users" for metric in REGISTRY.collect()):
    active_users_gauge = Gauge("active_users", "Number of active users in the system")
else:
    active_users_gauge = Gauge("active_users", "Number of active users in the system", registry=None)

@app.get("/") # path operation decorator
async def root():
    return {"message":"Hello World from FASTAPI"}

@app.get("/demo") # path operation decorator
def demo_func():
    demo_counter.inc() # Increment the counter
    start_time = time.time()
    result = {"message": "This is output from demo function"}
    latency = time.time() - start_time
    demo_latency_histogram.observe(latency) # record the latency
    return result

@app.post("/login") # path operation decorator
def demo_login():
    active_users_gauge.inc() # Increment the gauge for active users
    return {"Message":"User logged in successfully"}

@app.post("/logout") # path operation decorator
def demo_logout():
    active_users_gauge.dec() # decrement the gauge for active users
    return {"Message":"User logged out successfully"}

@app.post("/post_demo") # path operation decorator
def demo_post():
    return {"message":"This is output from post demo function"}

Instrumentator().instrument(app).expose(app) # /metrics endpoint will be available
# to expose the metrics
# You can access the metrics at http://localhost:8005/metrics

if __name__== "__main__":
    uvicorn.run("main:app", host="0.0.0.0",port=port,reload=False)

