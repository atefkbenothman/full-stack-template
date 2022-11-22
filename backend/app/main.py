from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    data = {
        "hello": "world"
    }
    return data
