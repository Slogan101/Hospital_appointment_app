from fastapi import APIRouter, status, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from ..database import get_db
from .. import Oauth2
from ..schemas.users import UserCreate, UserResponse, UserLogin
from ..services.users import user_crud



user_router = APIRouter()

@user_router.post("/", status_code=status.HTTP_201_CREATED, response_model=UserResponse)
def register_user(payload: UserCreate, db: Session = Depends(get_db)):
    new_user = user_crud.register_user(payload, db)
    return new_user


@user_router.post("/login", status_code=status.HTTP_200_OK)
def login_user(user_credtials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    logged_in = user_crud.login_user(db, user_credtials)
    return logged_in

@user_router.delete("/", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(db: Session = Depends(get_db), current_user: int = Depends(Oauth2.get_current_user)):
    user_crud.delete_user(db, current_user)