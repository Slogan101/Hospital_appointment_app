from pydantic import BaseModel
from datetime import date, time


class AppointmentCreate(BaseModel):
    doctor_id: int
    appointment_date: date
    time_slot: time
    is_completed: bool = False


class AvailalableAppointment(BaseModel):
    doctor_id: int
    appointment_date: date 

    
    

class AppointmentUpdate(BaseModel):
    is_completed: bool = False

class AppointmentResponse(BaseModel):
    doctor_id: int
    patient_id: int
    appointment_date: date
    time_slot: time
    is_completed: bool = False






