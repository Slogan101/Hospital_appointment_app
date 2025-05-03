from .. import models
from ..schemas.patient import Patient, PatientCreate, PatientUpadte, PatientResponse
from fastapi import HTTPException, status
from sqlalchemy.orm import Session



class PatientCrud:
    
    @staticmethod
    def get_patient(db: Session, current_user):
        patient = db.query(models.Patient).filter(models.Patient.id == current_user.id).first()
        if not patient:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Patient not found!")
        return patient
    
    @staticmethod
    def create_patient(patient: PatientCreate, current_user, db: Session):
        existing_patient = db.query(models.Patient).filter(models.Patient.id == current_user.id).first()
        if existing_patient:
            return {"Error": "User is already a patient."}
        
        new_patient = models.Patient(id=current_user.id, **patient.model_dump())
        db.query(models.User).filter(models.User.id == current_user.id).update({"role": "patient"})
        db.add(new_patient)
        db.commit()
        db.refresh(new_patient)
        return new_patient
    
    @staticmethod
    def update_patient(payload: PatientCreate, db: Session, current_user):
        patient_query = db.query(models.Patient).filter(models.Patient.id == current_user.id)
        patient_query.update(payload.model_dump(), synchronize_session=False)
        db.commit()
        return patient_query.first()
    
    @staticmethod
    def partially_upadte_patient(payload: PatientUpadte, db: Session, current_user):
        patient_query = db.query(models.Patient).filter(models.Patient.id == current_user.id)
        patient_query.update(payload.model_dump(exclude_unset=True), synchronize_session=False)
        db.commit()
        return patient_query.first()
    
      








patient_crud = PatientCrud()