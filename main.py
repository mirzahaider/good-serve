from fastapi import FastAPI
import random


app = FastAPI()


@app.get("/")
def ret():
    random_number = random.randint(1, 100)
    return f"This is a beautiful world - fact:{random_number}"
