import os
from dotenv import load_dotenv
from fastapi import FastAPI
from api.router import api_router

from models.database import Base, engine


load_dotenv(verbose=True, override=True)


# setting mode and url, port
mode: str = "DEVELOPMENT"


def get_url_port(): return [
    os.getenv(f"{mode}_URL"), int(os.getenv(f"{mode}_PORT"))]


[url, port] = get_url_port()


# init DB
Base.metadata.create_all(bind=engine)

# init app
app = FastAPI()

app.include_router(api_router, prefix="/api")


# if __name__ == "__main__":
#     uvicorn.run("main:app", host=url, port=port, reload=True)
