from pydantic import BaseModel
from pydantic import BaseModel, EmailStr
from datetime import time



class DoctorBase(BaseModel):
    name: str
    age: int
    sex: str
    specialization: str
    experience: int
    phone_num: str
    license_num: str
    is_available: bool = True 


class DoctorCreate(DoctorBase):
    pass

class Doctor(DoctorBase):
    id: int

class DoctorUpdate(BaseModel):
    name: str | None = None
    age: int | None = None
    sex: str | None = None
    specialization: str | None = None
    experience: int | None = None
    phone_num: str | None = None
    license_num: str | None = None
    is_available: bool = True 

class DoctorStatus(BaseModel):
    is_available: bool | None = None

class DoctorResponse(DoctorBase):
    email: EmailStr | None = None









