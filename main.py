from fastapi import FastAPI
from webdriver_manager.chrome import ChromeDriverManager

from auto import get_dawn_columns


app = FastAPI()

# Install Chrome binaries
driver_manager = ChromeDriverManager()
driver_manager.install()

@app.get("/")
def ret():
    articles = get_dawn_columns()
    return articles
