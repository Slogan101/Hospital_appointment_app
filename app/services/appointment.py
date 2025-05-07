from ..schemas.appointment import AppointmentCreate, AppointmentResponse, AppointmentUpdate, AvailalableAppointment
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from .. import models
from datetime import datetime, timezone, timedelta, time
from ..utils import generate_meeting_link


WORKING_HOURS = range(9, 16)
ALLOWED_WEEKDAYS = range(0, 5)

class AppointmentCrud():
    @staticmethod
    def create_appointment(payload: AppointmentCreate, db: Session, current_user):
        min_date = datetime.now(timezone.utc).date() + timedelta(days=2)  # Ensure at least 2 days ahead
        appointment_date = payload.appointment_date
        appointment_time = payload.time_slot.hour
        appointment_time_str = payload.time_slot.strftime("%H:%M")
        


        #check if the ID is a patient
        patient_query = db.query(models.User).filter(models.User.id == current_user.id)
        patient = patient_query.first()
        if patient.role !="patient":
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Only patients are allowed to book an appointment.")
        if not patient:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found!")
        if patient:
            patient_main = db.query(models.Patient).filter(models.Patient.id == current_user.id).first()
        
       
        
        # Check if the doctor ID passed exists and is actually a doctor
        doctor_query = db.query(models.User).filter(models.User.id == payload.doctor_id)
        user_doctor = doctor_query.first()
        if not user_doctor:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Doctor not found!")
        if doctor_query.first().role != "doctor":
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="You can only book appointment with a doctor!")
        if user_doctor:
            doctor_main = db.query(models.Doctor).filter(models.Doctor.id == payload.doctor_id).first()
        
        #Checks the doctors time_slots and confirms if the time entered by the patient is free for the doctor.

        booked_slots = db.query(models.Appointment.time_slot).filter(models.Appointment.doctor_id == payload.doctor_id, models.Appointment.appointment_date == payload.appointment_date).all()
        booked_times = [slot[0].strftime("%H:%M") for slot in booked_slots]
        if appointment_time_str in booked_times:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="sorry, doctor is unavailable.")
        # Checks if the date that the patient input is 2 days ahead.
        if appointment_date < min_date:
            raise HTTPException(status_code=400, detail="Appointment must be at least 2 days from today.")

        # Restrict weekends from being booked (Saturday=5, Sunday=6)
        if appointment_date.weekday() not in ALLOWED_WEEKDAYS:
            raise HTTPException(status_code=400, detail="Appointments can only be booked on weekdays (Monday–Friday).")

        # Restrict time slots to working hours
        if appointment_time not in WORKING_HOURS:
            raise HTTPException(status_code=400, detail="Appointments must be scheduled between 9:00 AM and 4:00 PM.")
        
        meeting_link = generate_meeting_link(doctor_main.name, patient_main.name)
        new_appointment = models.Appointment(patient_id=current_user.id, meeting_link=meeting_link, **payload.model_dump())
        db.query(models.Doctor).filter(models.Doctor.id == payload.doctor_id).update({"is_available": False})
        db.add(new_appointment)
        db.commit()
        return {
        "id": new_appointment.id,
        "appointment_date": new_appointment.appointment_date,
        "time_slot": new_appointment.time_slot,
        "meeting_link": new_appointment.meeting_link,
        "doctor_name": doctor_main.name,  # assuming relationship is defined
        "patient_name": patient_main.name  # assuming relationship is defined
    }
    

    @staticmethod
    def get_appointment(db: Session, current_user):
        if current_user.role == "patient":
            appointments = db.query(models.Appointment).filter(models.Appointment.patient_id == current_user.id).all()
            return appointments
        elif current_user.role == "doctor":
            appointments = db.query(models.Appointment).filter(models.Appointment.doctor_id == current_user.id).all()
            print(appointments)
            return appointments
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Sorry no appointment record for you!")
    

    @staticmethod
    def check_available_slots(payload: AvailalableAppointment, db: Session, current_user):
        all_slots = [time(hour, 0) for hour in WORKING_HOURS]
        try:
             selected_date = payload.appointment_date
            # datetime.strptime(str(payload.appointment_date), "%Y-%m-%d").date()
        except ValueError:
            return {"Error": "Invalid date format. Use YYYY-MM-DD."}
        
        # Restrict the weekends
        if selected_date.weekday() not in ALLOWED_WEEKDAYS:
            raise HTTPException(status_code=400, detail="Appointments can only be booked on weekdays (Monday–Friday).")
        
        booked_slots = db.query(models.Appointment.time_slot).filter(models.Appointment.doctor_id == payload.doctor_id, models.Appointment.appointment_date == selected_date).all()
        booked_times = [slot[0].strftime("%H:%M") for slot in booked_slots]
        available_slots = [slot.strftime("%H:%M") for slot in all_slots if slot.strftime("%H:%M") not in booked_times]
 

        return {"date": payload.appointment_date, "available_slots": available_slots}





        

        

    # @staticmethod
    # def get_appointment(id):
    #     appointment = next((point for point in appointment_db if point.appointment_id == id), None)
    #     if not appointment:
    #         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No appointment found!")
    #     return appointment
    
    # @staticmethod
    # def complete_appointment(appointment, data: AppointmentUpdate):

    #     update_data = data.model_dump(exclude_unset=True).items()
    #     for k,v in update_data:
    #         setattr(appointment, k, v)


    #     patient = next((pat for pat in patient_db if pat.id == appointment.patient_id), None)
    #     doctor = next((doc for doc in doctor_db if doc.id == appointment.doctor_id), None)
    #     response = AppointmentResponse(
    #         patient = patient.name,
    #         doctor = doctor.name,
    #         date = appointment.date,
    #         is_completed = appointment.is_completed
    #     )
       
    #     doctor.is_available = True

        
    

        # return response






appointment_crud = AppointmentCrud()