from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime

# Pydantic schema for creating a goal
class GoalCreate(BaseModel):
  title: str
  target: float
  current_target: Optional[float] = 0
  description: Optional[str] = None
  members: List[EmailStr] = []

# Pydantic schema for reading goals
class UserOut(BaseModel):
  id: int
  name: str
  email: EmailStr

  class config:
    orm_mode = True

class GoalMemberOut(BaseModel):
  id: int
  name: str
  email: EmailStr
  role: str
  total_contributed: float
  last_activity: Optional[datetime]
  
class GoalRead(BaseModel):
  id: int
  title: str
  target: float
  current_target: float
  description: Optional[str] = None
  members: List[UserOut] = []

  class config:
    orm_mode = True

class GoalDropdown(BaseModel):
  id: int
  title: str

  class config:
    orm_mode = True

class DepositRequest(BaseModel):
  amount: float

class GoalMembersResponse(BaseModel):
  members: List[GoalMemberOut]