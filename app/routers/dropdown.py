from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session, joinedload
from typing import List
from app.models.goal import GoalDropdown, GoalRead
from app.database.models.goal_model import Goal
from app.database.models.user_model import User
from app.db import get_db
from app.core.security import get_current_user

router = APIRouter(prefix="/api/dropdown", tags=["Dropdown"])

@router.get("/goals", response_model=List[GoalDropdown])
def get_goals_dropdown(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
  """ 
  Get goals dropdown
  """

  goalsDropdown = db.query(Goal.id, Goal.title).filter(Goal.members.any(id=current_user.id)).all()

  return goalsDropdown