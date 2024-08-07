from fastapi import APIRouter
from .users import user_router
from .langchain import langchain_router
from .classify import classify_router
api_router = APIRouter()

api_router.include_router(
    langchain_router, prefix="/langchain", tags=["langchain"])
api_router.include_router(user_router, prefix="/user", tags=["user"])
api_router.include_router(
    classify_router, prefix='/classify', tags=["classify"])
