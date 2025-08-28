from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session, joinedload
from typing import List
from app.models.goal import GoalCreate, GoalRead
from app.database.models.goal_model import Goal
from app.database.models.association import goal_members
from app.database.models.user_model import User
from app.db import get_db
from app.core.security import get_current_user

router = APIRouter(prefix="/api/goals", tags=["Goals"])

@router.post("/")
def create_goal(goal:GoalCreate, db: Session = Depends(get_db)):
  """ 
  Create a new goal
  """

  db_goal = Goal(
    title=goal.title,
    target=goal.target,
    current_target= 0,
    description=goal.description
  )

  # Add members by email
  for email in goal.members:
    user = db.query(User).filter(User.email == email).first()
    if not user:
      raise HTTPException(
        status_code=404, 
        detail=f"User with email {email} not found"
      )
    db_goal.members.append(user)

  db.add(db_goal)
  db.commit()
  db.refresh(db_goal)
  return db_goal

@router.get("/", response_model=List[GoalRead])
def get_goals(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
  """
  Get all goals that belongs to the logged-in user with members
  """
  goals = db.query(Goal).options(joinedload(Goal.members)).filter(Goal.members.any(id=current_user.id)).all()
  return goals

@router.post("/{goal_id}/deposit")
def deposit_to_goal(goal_id: int, amount: float, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
  """ 
  Deposit an amount to a specific goal
  Only members of the goal can deposit
  """

  # Check goal exist
  goal = db.query(Goal).filter(Goal.id == goal_id).first()
  if not goal:
    raise HTTPException(status_code=404, detail="Goal not found")
  
  # Check if user is a member of the goal
  member = (
    db.query(goal_members)
    .filter(goal_members.c.goal_id == goal_id, goal_members.c.user_id == current_user.id)
    .first()
    )
  
  if not member:
    raise HTTPException(
      status_code=status.HTTP_403_FORBIDDEN,
      detail="You are not a member of this goal"
    )
  
  # update current_target
  goal.current_target += amount
  db.commit()
  db.refresh(goal)

  return {
    "message" : "Deposit successful",
    "goal": {
      "id" : goal.id,
      "title" : goal.title,
      "target" : goal.target,
      "current_target" : goal.current_target
    }
  }