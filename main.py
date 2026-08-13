from fastapi import FastAPI

from database import engine, Base
import models
from routers import router


Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Product Management API",
    version="1.0.0"
)


app.include_router(router)


@app.get("/")
def home():

    return {
        "message": "Welcome to Product Management API"
    }