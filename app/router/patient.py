from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..database import get_db
from .. import Oauth2
from ..services.patient import patient_crud
from ..schemas.patient import PatientResponse, PatientCreate, PatientUpadte


patient_router = APIRouter()


# @patient_router.get("/", response_model=list[PatientResponse], status_code=status.HTTP_200_OK)
# def get_patients(db: Session = Depends(get_db)):
#     patients = patient_crud.get_patients(db)
#     return patients

@patient_router.get("/", response_model=PatientResponse, status_code=status.HTTP_200_OK)
def get_patient( db: Session = Depends(get_db), current_user: int = Depends(Oauth2.get_current_user)):
    patient = patient_crud.get_patient(db, current_user) 
    return patient

@patient_router.post("/", response_model=PatientResponse, status_code=status.HTTP_201_CREATED)
def create_patient(payload: PatientCreate, db: Session = Depends(get_db), current_user: int = Depends(Oauth2.get_current_user)):
    new_patient = patient_crud.create_patient(payload, current_user, db)
    return new_patient

@patient_router.put("/", response_model=PatientResponse, status_code=status.HTTP_200_OK)
def update_patient(payload: PatientCreate, db: Session = Depends(get_db), current_user: int = Depends(Oauth2.get_current_user)):
    # patient = patient_crud.get_patient(db, current_user)
    updated_patient = patient_crud.update_patient(payload, db, current_user)
    return updated_patient

@patient_router.patch("/", response_model=PatientResponse, status_code=status.HTTP_200_OK)
def partially_upadte_patient(payload: PatientUpadte, db: Session = Depends(get_db), current_user: int = Depends(Oauth2.get_current_user)):
    patient_update = patient_crud.partially_upadte_patient(payload, db, current_user)
    return patient_update

