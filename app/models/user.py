from pydantic import BaseModel, EmailStr, field_validator
from pydantic_core import PydanticCustomError

# Schema user
class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str

    @field_validator("name")
    def validate_name(cls, v):
        if len(v.strip()) < 1:
            raise PydanticCustomError(
                "name_too_short", 
                "name should have at least 1 character"
            )
        if len(v) > 50:
            raise PydanticCustomError(
                "name_too_long", 
                "name should have at most 50 characters"
            )
        return v
    
    @field_validator("password")
    def validate_password(cls, v):
        if len(v) < 6:
            raise PydanticCustomError(
                "password_too_short", 
                "password should have at least 6 characters"
            )
        return v
