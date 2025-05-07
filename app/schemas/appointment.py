from pydantic import BaseModel
from datetime import date, time
from uuid import UUID


class AppointmentCreate(BaseModel):
    doctor_id: UUID
    appointment_date: date
    time_slot: time
    is_completed: bool = False


class AvailalableAppointment(BaseModel):
    doctor_id: UUID
    appointment_date: date 

    
    

class AppointmentUpdate(BaseModel):
    is_completed: bool = False

class AppointmentResponse(BaseModel):
    doctor_name: str
    patient_name: str
    appointment_date: date
    time_slot: time
    meeting_link: str
    is_completed: bool = False






