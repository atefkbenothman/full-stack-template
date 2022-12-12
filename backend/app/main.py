import time
import random

from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

from .metrics import backend_requests_total 


app = FastAPI()

# setup prometheus
Instrumentator().instrument(app).expose(app)


@app.get("/hello")
def read_root():
    sleep_time = random.randint(1, 3)
    time.sleep(sleep_time)
    data = {
        "hello": "world"
    }
    backend_requests_total.labels("/hello").inc()
    return data


@app.get("/test")
def read_test():
    data = {
        "test": "123",
        "ping": "pong"
    }
    backend_requests_total.labels("/test").inc()
    return data
