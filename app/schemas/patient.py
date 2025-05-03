from pydantic import BaseModel, EmailStr


class PatientBase(BaseModel):
    name: str
    age: int
    sex: str
    weight: float
    phone_num: str
    Emergency_contact_name: str
    Emergency_contact_phone_num: str
    known_medical_conditions: str|None
    current_medications: str|None
    insurance_provider: str|None

class PatientCreate(PatientBase):
    pass

class Patient(PatientBase):
    id: int

class PatientUpadte(BaseModel):
    name: str | None = None
    age: int | None = None
    sex: str | None = None
    weight: float | None = None
    contact: str | None = None
    Emergency_contact_name: str|None = None
    Emergency_contact_phone_num: str|None = None
    known_medical_conditions: str|None = None
    current_medications: str|None = None
    insurance_provider: str|None = None

class PatientResponse(PatientBase):
    pass














