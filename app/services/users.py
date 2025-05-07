from ..schemas.users import UserCreate, User, UserLogin
from ..schemas.token import Token
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from .. import models, Oauth2
from ..utils import hash_password, confirm_credentials




class UserCrud:
    @staticmethod
    def register_user(user: UserCreate, db: Session):
      password = hash_password(user.password)
      user.password = password
      new_user = models.User(**user.model_dump())
      db.add(new_user)
      db.commit()
      db.refresh(new_user)
      return new_user
    

    @staticmethod
    def login_user(db: Session, user_credentials: OAuth2PasswordRequestForm = Depends()):
       user = db.query(models.User).filter(models.User.email == user_credentials.username).first()
       if not user:
          raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Credentials!")
       confirm = confirm_credentials(user_credentials.password, user.password)
       if not confirm:
          raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Credentials!")
       access_token = Oauth2.create_access_token(data={"user_id": str(user.id), "user_role":user.role})

       response = Token(
          access_token = access_token,
          token_type = "bearer"
       )

       return response
    
    @staticmethod
    def delete_user(db: Session, current_user):
       user_query = db.query(models.User).filter(models.User.id == current_user.id)
       user_query.delete(synchronize_session=False)
       db.commit()
       return {"data": "User successfully deleted."}






user_crud = UserCrud()