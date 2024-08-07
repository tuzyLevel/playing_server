from pydantic import BaseModel, Field
from datetime import datetime


class Chat(BaseModel):
    filename: str = Field(..., description="파일명")
    description: str = Field(..., description="파일 상세 정보")
    created_at: datetime = Field(..., description="생성일자, 최종 수정일로 해야됨")
