from pydantic import BaseModel, Field


class LangchainRequestBase(BaseModel):
    message: str = Field(..., description="user question")
