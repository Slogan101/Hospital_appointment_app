from fastapi import APIRouter, status, Depends
from ..schemas.doctor import Doctor, DoctorCreate, DoctorUpdate, DoctorStatus, DoctorResponse
from ..services.doctor import doc_crud
from sqlalchemy.orm import Session
from .. import Oauth2
from ..database import get_db

doc_router = APIRouter()


# @doc_router.get("/", response_model=list[DoctorResponse], status_code=status.HTTP_200_OK)
# def get_doctors():
#     doctors = doc_crud.get_doctors()
#     return doctors

@doc_router.get("/", response_model=DoctorResponse, status_code=status.HTTP_200_OK)
def get_doctor(db: Session = Depends(get_db), current_user: int = Depends(Oauth2.get_current_user)):
    doctor = doc_crud.get_doctor(db, current_user)
    return doctor

@doc_router.post("/", response_model=DoctorResponse, status_code=status.HTTP_201_CREATED)
def create_doctor(payload: DoctorCreate, db: Session = Depends(get_db), current_user: int = Depends(Oauth2.get_current_user)):
    new_doctor = doc_crud.create_doctor(payload, db, current_user)
    return new_doctor

@doc_router.put("/", response_model=DoctorResponse, status_code=status.HTTP_200_OK)
def update_doctor(payload: DoctorCreate, db: Session = Depends(get_db), current_user: int = Depends(Oauth2.get_current_user)):
    updated_doctor = doc_crud.update_doctor(payload, db, current_user)
    return updated_doctor

@doc_router.patch("/", response_model=DoctorResponse, status_code=status.HTTP_200_OK)
def partially_update_doctor(payload: DoctorUpdate, db: Session = Depends(get_db), current_user: int = Depends(Oauth2.get_current_user)):
    partial_update_doc = doc_crud.partially_update_doctor(payload, db, current_user)
    return partial_update_doc

@doc_router.patch("/status", response_model=DoctorResponse, status_code=status.HTTP_200_OK)
def available_status(payload: DoctorStatus, db: Session = Depends(get_db), current_user: int = Depends(Oauth2.get_current_user)):
    avail_stats = doc_crud.available_status(payload, db, current_user)
    return avail_stats
