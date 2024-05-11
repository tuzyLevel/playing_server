from fastapi import FastAPI
import uvicorn
import os
import dotenv


dotenv.load_dotenv()

port = os.getenv("PORT")

app = FastAPI()


@app.get("/")
def main():
    return "Hello"


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
