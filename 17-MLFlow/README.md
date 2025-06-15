```bash
mlflow server --default-artifact-root ./mlruns --host 0.0.0.0 --port 5001

mlflow ui

python train.py

```

# MLFLow Serving

```bash
mlflow models serve -m runs:/68d53dd541ff4570a0f6405c78c9ae89/model -p 5005
```

# Postman settings

URL : http://127.0.0.1:5005/invocations
```json

{
    "instances": [[0.045341,-0.044642,-0.006206,-0.015999,0.125019,0.125198,0.019187,0.034309,0.032432,-0.005220]]
}

```