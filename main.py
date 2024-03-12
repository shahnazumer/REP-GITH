from typing import Union
from fastapi import FastAPI 
app = FastAPI()

#Test Route
@app.get("/test")
def read_root():
    return {"Hello": "World"}
