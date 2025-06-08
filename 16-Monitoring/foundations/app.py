from fastapi import FastAPI
from prometheus_client import start_http_server,generate_latest, CONTENT_TYPE_LATEST
from monitor import monitor
import pandas as pd
import time
import threading
from fastapi.responses import Response
import uvicorn
app = FastAPI()

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)

def background_monitoring():
    while True:
        monitor()
        time.sleep(60)

if __name__ == "__main__":
    start_http_server(8001)
    thread = threading.Thread(target=background_monitoring, daemon=True)
    thread.start()
    uvicorn.run(app, host="0.0.0.0", port=8000)



