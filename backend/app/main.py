import time
import random

from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
from prometheus_client import (
    start_http_server,
    Summary,
    Counter,
    Info,
)

app = FastAPI()

# prometheus
# start_http_server(3002)

# info = Info(
#     name="app",
#     documentation="info about application"
# )
# info.info(
#     {
#         "version": "1.0",
#         "language": "python",
#         "framework": "fastapi"
#     }
# )
# requests_total = Counter(
#     name="app_requests_total",
#     documentation="total number of requests",
#     labelnames=["endpoint", "method"]
# )
# read_root_run_time = Summary(
#     name="app_read_root_run_time_seconds",
#     documentation="time to run read_root method"
# )

Instrumentator().instrument(app).expose(app)
backend_requests_total = Counter(
    name="backend_requests_total",
    documentation="Total number of http requests made to the backend.",
    labelnames=["endpoint"],
)


@app.get("/")
def read_root():
    sleep_time = random.randint(1, 3)
    time.sleep(sleep_time)
    data = {
        "hello": "world"
    }
    # requests_total.labels(endpoint="/", method="GET").inc()
    # read_root_run_time.observe(sleep_time)
    backend_requests_total.labels("/").inc()
    return data


@app.get("/test")
def read_test():
    data = {
        "test": "123"
    }
    backend_requests_total.labels("/test").inc()
    return data
