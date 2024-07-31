from fastapi import FastAPI
from src.logger import logger

app = FastAPI()

@app.get("/")
def read_root():
    logger.info("Logged a message")
    return {"msg": "This is the root of service1."}


