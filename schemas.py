from pydantic import BaseModel, EmailStr


class Contact(BaseModel):
    name: str
    email: EmailStr
    service: str
    phonenumber: str