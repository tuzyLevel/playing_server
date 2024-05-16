from pydantic import BaseModel, Field


class UserBase(BaseModel):
    email: str = Field(..., description="email")


class UserAuthBaseSchema(UserBase):
    password: str = Field(..., description="password")


class CreateUserSchema(UserAuthBaseSchema):
    password_validation: str = Field(..., description="password_validation")


class RequestDummyUserSchema(UserBase):
    pass
