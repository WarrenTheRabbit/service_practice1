from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"msg": "This is the root of service1."}


