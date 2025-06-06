from pydantic import BaseModel, Field, EmailStr, constr

from tools.fakers import get_random_email


class UserSchema(BaseModel):
    """
    Pydantic-модель данных пользователя
    """
    id: str
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")


class CreateUserRequestSchema(BaseModel):
    """
    Pydantic-модель данных запроса на создание пользователя
    """
    email: EmailStr = Field(default_factory=get_random_email)
    password: constr(min_length=6, max_length=15) = "qwerty12345"
    last_name: str = Field(alias="lastName", default="Bond")
    first_name: str = Field(alias="firstName", default="Zara")
    middle_name: str = Field(alias="middleName", default="Alice")


class CreateUserResponseSchema(BaseModel):
    """
    Pydantic-модель данных ответа на запрос создания пользователя
    """
    user: UserSchema
