from fastapi import FastAPI

from auto import get_dawn_columns


app = FastAPI()


@app.get("/")
def ret():
    articles = get_dawn_columns()
    return articles
