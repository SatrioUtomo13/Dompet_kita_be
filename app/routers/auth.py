from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database.models.user_model import User
from app.models.login import LoginRequest
from app.db import get_db
from app.core.security import verify_password, create_access_token

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/login")
def login(request: LoginRequest, db: Session = Depends(get_db)):
  user = db.query(User).filter(User.email == request.email).first()
  if not user:
    raise HTTPException(
      status_code=status.HTTP_401_UNAUTHORIZED,
      detail="Invalid email or password"
    )
  
  if not verify_password(request.password, user.password):
    raise HTTPException(
      status_code=status.HTTP_401_UNAUTHORIZED,
      detail="Invalid email or password"
    )
  
  token = create_access_token({"sub": user.email})
  return {"access_token": token, "token_type": "bearer"}