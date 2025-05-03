from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(user_password):
    hashed_password = pwd_context.hash(user_password)
    return hashed_password

def confirm_credentials(user_password, hashed_password):
    confirm = pwd_context.verify(user_password, hashed_password)
    return confirm