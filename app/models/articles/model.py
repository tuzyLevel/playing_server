from sqlalchemy import Boolean, Column, Integer, String, DateTime, func
from sqlalchemy.orm import relationship


from ..database import Base


class DefaultBase:
    id_deleted = Column(Boolean, default=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now())


class Article(Base, DefaultBase):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True)
    title = Column(String(50), index=True)
    content = Column(String(500))
    read_count = Column(Integer, default=0)
