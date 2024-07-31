from fastapi import FastAPI, Request
from src.logger import logger

app = FastAPI()
logger.info("Starting service1...")


@app.middleware("http")
async def log_middleware(request: Request, call_next):
    log_dict = {
        'url': request.url.path,
        'method': request.method,
    }
    logger.info(log_dict)
    
    response = await call_next(request)
    return response


@app.get("/")
def read_root(request: Request):
    return {"msg": "This is the root of service1."}



