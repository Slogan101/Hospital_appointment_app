from ..schemas.doctor import Doctor, DoctorCreate, DoctorUpdate, DoctorStatus, DoctorResponse
from fastapi import HTTPException, status, Depends
from sqlalchemy.orm import Session
from .. import models



class DocCrud:
    # @staticmethod
    # def get_doctors():
    #     return doctor_db
    
    @staticmethod
    def get_doctor(db: Session, current_user):
        doctor = db.query(models.Doctor).filter(models.Doctor.id == current_user.id).first()
        if not doctor:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Doctor not found!")
        return doctor
    
    @staticmethod
    def create_doctor(doctor: DoctorCreate, db: Session, current_user):
        existing_doctor = db.query(models.Doctor).filter(models.Doctor.id == current_user.id).first()
        if existing_doctor:
            return {"Error": "User already a doctor!"}
        
        new_doctor = models.Doctor(id=current_user.id, **doctor.model_dump())
        db.query(models.User).filter(models.User.id == current_user.id).update({"role": "doctor"})
        db.add(new_doctor)
        db.commit()
        db.refresh(new_doctor)
        return new_doctor
    
    @staticmethod
    def update_doctor(payload: DoctorCreate, db: Session, current_user):
        doctor_query = db.query(models.Doctor).filter(models.Doctor.id == current_user.id)
        doctor_query.update(payload.model_dump(), synchronize_session=False)
        db.commit()
        db.refresh(doctor_query.first())
        return doctor_query.first()
    
    @staticmethod
    def partially_update_doctor(payload: DoctorUpdate, db: Session, current_user):
        doctor_query = db.query(models.Doctor).filter(models.Doctor.id == current_user.id)
        doctor_query.update(payload.model_dump(exclude_unset=True), synchronize_session=False)
        db.commit()
        return doctor_query.first()
    
    @staticmethod
    def available_status(payload:DoctorStatus, db: Session, current_user):
        doctor_query = db.query(models.Doctor).filter(models.Doctor.id == current_user.id)
        doctor_query.update(payload.model_dump(exclude_unset=True), synchronize_session=False)
        db.commit()
        return doctor_query.first()
    




doc_crud = DocCrud()