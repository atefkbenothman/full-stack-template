from prometheus_client import Counter

backend_requests_total = Counter(
    name="backend_requests_total",
    documentation="Total number of http requests made to the backend.",
    labelnames=["endpoint"],
)
