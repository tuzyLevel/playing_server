from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.users.schema import CreateUserSchema, RequestDummyUserSchema
from models.users.crud import (
    get_user, create_user, get_user_by_email, get_users)
from models.database import get_db


user_router = APIRouter()


@user_router.post("/")
def create_user_end_point(user: CreateUserSchema, db: Session = Depends(get_db)):

    db_user = get_user_by_email(db=db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already Exists")
    return create_user(db=db, user=user)


@user_router.get("/")
async def get_user(request_schema: RequestDummyUserSchema):
    return get_user


@user_router.get("/users")
def get_user_fuction(db: Session = Depends(get_db)):
    return get_users(db=db)
