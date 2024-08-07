from fastapi import APIRouter, HTTPException
from .model import get_answer
from pydantic import Field
from schemas.langchain.schema import LangchainRequestBase

langchain_router = APIRouter()


@langchain_router.post("/")
def get_riot_id_info(request_params: LangchainRequestBase):
    output = get_answer(request_params.message)
    return output


@langchain_router.get("/test")
def get_riot_champions_rotation(server: str):

    return "test2"
