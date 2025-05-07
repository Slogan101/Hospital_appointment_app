import uuid
from .database import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, NUMERIC, Enum, Date, Time
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from sqlalchemy.dialects.postgresql import UUID




class User(Base):
    __tablename__ = "users"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    role = Column(Enum("patient", "doctor", name="user_roles"), nullable=True)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))



class Patient(Base):
    __tablename__ = "patients"
    id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    sex = Column(String, nullable=False)
    weight = Column(NUMERIC(10,2), nullable=True)
    phone_num = Column(String, nullable=False)
    Emergency_contact_name = Column(String, nullable=False)
    Emergency_contact_phone_num = Column(String, nullable=False)
    known_medical_conditions = Column(String, nullable=True)
    current_medications = Column(String, nullable=True)
    insurance_provider = Column(String, nullable=True)
    
    user = relationship("User")
    

class Doctor(Base):
    __tablename__ = "doctors"
    id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    name = Column(String, nullable=False)
    age = Column(String, nullable=False)
    sex = Column(String, nullable=False)
    specialization = Column(String, nullable=False)
    experience = Column(Integer, nullable=True)
    phone_num = Column(String, nullable=False)
    license_num = Column(String, nullable=False)
    is_available = Column(Boolean, default=True, nullable=False)
    
    user = relationship("User")



class Appointment(Base):
    __tablename__ = "appointment"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    patient_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    doctor_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    is_completed = Column(Boolean, server_default="False", nullable=False)
    appointment_date = Column(Date, nullable=False)
    meeting_link = Column(String, nullable=True)
    time_slot = Column(Time, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))
    
    patient = relationship("User", foreign_keys=[patient_id])
    doctor = relationship("User", foreign_keys=[doctor_id])
    













