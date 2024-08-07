from pydantic import BaseModel
from datetime import datetime


class Chat(BaseModel):
    role: str
    user_id: str
    created_at: datetime
