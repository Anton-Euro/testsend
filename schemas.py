from pydantic import BaseModel, EmailStr


class Contact(BaseModel):
    name: str
    email: EmailStr
    service: str
    phone: str
    consent: bool