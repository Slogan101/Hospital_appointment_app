from fastapi import APIRouter, status, Depends
from ..services.appointment import appointment_crud
from ..schemas.appointment import AppointmentCreate, AppointmentResponse, AppointmentUpdate, AvailalableAppointment
from sqlalchemy.orm import Session
from .. import Oauth2
from ..database import get_db


appoint_router = APIRouter()

@appoint_router.post("/", response_model=AppointmentResponse, status_code=status.HTTP_201_CREATED)
def create_appointment(payload: AppointmentCreate, db: Session = Depends(get_db), current_user: int = Depends(Oauth2.get_current_user)):
    appointment = appointment_crud.create_appointment(payload, db, current_user)
    return appointment

@appoint_router.get("/", response_model=list[AppointmentResponse], status_code=status.HTTP_200_OK)
def get_appointment(db: Session = Depends(get_db), current_user: int = Depends(Oauth2.get_current_user)):
    appointments = appointment_crud.get_appointment(db, current_user)
    return appointments

@appoint_router.post("/doctor", status_code=status.HTTP_200_OK)
def get_availabile_slots(payload: AvailalableAppointment, db: Session = Depends(get_db), current_user: int = Depends(Oauth2.get_current_user)):
    available_slots = appointment_crud.check_available_slots(payload, db, current_user)
    return available_slots
    

# @appoint_router.patch("/{id}", response_model=AppointmentResponse)
# def complete_appointment(id: int, data: AppointmentUpdate):
#     appointment = appointment_crud.get_appointment(id)
#     completed_appointment = appointment_crud.complete_appointment(appointment, data)
#     return completed_appointment