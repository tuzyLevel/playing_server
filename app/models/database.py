import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


# database
database_url = os.getenv("DATABASE_URL")
engine = create_engine(database_url)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
