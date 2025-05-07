from passlib.context import CryptContext
import uuid


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(user_password):
    hashed_password = pwd_context.hash(user_password)
    return hashed_password

def confirm_credentials(user_password, hashed_password):
    confirm = pwd_context.verify(user_password, hashed_password)
    return confirm





def generate_meeting_link(doctor_name: str, patient_name: str):
    safe_doctor = doctor_name.replace(" ", "")
    safe_patient = patient_name.replace(" ", "")
    unique = uuid.uuid4().hex[:6]
    return f"https://meet.jit.si/{safe_doctor}-{safe_patient}-{unique}"
