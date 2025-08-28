from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone
from jose import jwt
import os
from dotenv import load_dotenv
from app.database.models.user_model import User
from app.db import get_db

Bearer = HTTPBearer()

# oauth2_scheme = OAuth2PasswordBearer(tokenUrl=None)

load_dotenv()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def hash_password(password: str) -> str:
  return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
  return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict, expires_delta: timedelta | None = None):
  to_encode = data.copy()
  expire = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
  to_encode.update({"exp": expire})
  encode_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
  return encode_jwt

# def get_current_user(token: str = Depends(Bearer), db: Session = Depends(get_db)):
#   try:
#     payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#     user_email: str = payload.get("sub")
#     if user_email is None:
#       raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")

#     user = db.query(User).filter(User.email == user_email).first()
#     print("querid user", user)
#     if user is None:
#       raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found")
    
#     return user
  
#   except jwt.JWTError:
#     raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
  

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(Bearer), db: Session = Depends(get_db)):
    token = credentials.credentials  # <-- ambil string token
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_email: str = payload.get("sub")
        if user_email is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")

        user = db.query(User).filter(User.email == user_email).first()
        if user is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found")
        
        return user
    
    except jwt.JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")