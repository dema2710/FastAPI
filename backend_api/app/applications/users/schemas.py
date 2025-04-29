from pydantic import BaseModel, EmailStr, Field

class UserFields(BaseModel):
    email: EmailStr = Field(description="User email", examples=['MD2710@ukr.net'])