from sqlalchemy.orm import Session

from models.users import model
from schemas.users import schema


def get_user(db: Session, user_id: int):
    return db.query(model.User).filter(model.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    try:
        return db.query(model.User).filter(model.User.email == email).first()
    except Exception as e:
        print(e)
        return True


async def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schema.CreateUserSchema):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = model.User(
        email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
