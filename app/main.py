from fastapi import FastAPI
from .router.patient import patient_router
from .router.doctor import doc_router
from .router.appointment import appoint_router
from .router.users import user_router
from .database import engine
from . import models





models.Base.metadata.create_all(bind=engine)



app = FastAPI()
app.include_router(patient_router, prefix="/patient", tags=["Patient"])
app.include_router(doc_router, prefix="/doctor", tags=["Doctor"])
app.include_router(appoint_router, prefix="/appointment", tags=["Appointment"])
app.include_router(user_router, prefix="/users", tags=["Users"])





@app.get("/")
def root():
    return {"message: Welcome to the hospital app!"}


