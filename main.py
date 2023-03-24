from fastapi import FastAPI

app = FastAPI()

from datadog import initialize, statsd

options = {
    'statsd_host': '127.0.0.1',
    'statsd_port': 8125
}

initialize(**options)


@app.get("/")
async def root():
    statsd.increment('hello-world-business-metric.increment', tags=["environment:local"])
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
