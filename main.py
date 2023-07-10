from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def ret():
    return "This is a beautiful world."
