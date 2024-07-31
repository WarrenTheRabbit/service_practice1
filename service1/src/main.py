from fastapi import FastAPI, Request

from starlette.middleware.base import BaseHTTPMiddleware

from src.middleware import log_middleware
from src.logger import logger


app = FastAPI()
app.add_middleware(BaseHTTPMiddleware, dispatch=log_middleware)
logger.info("Starting service1...")


@app.get("/")
def read_root(request: Request):
    return {"msg": "This is the root of service1."}



