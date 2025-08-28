from pydantic import BaseModel
from typing import Optional

# Pydantic schema for creating a group
class GroupCreate(BaseModel):
    name: str
    description: Optional[str] = None

# Schema for user contribution
class ContributionCreate(BaseModel):
    user_id: int
    amount: float
    role: str
    note: Optional[str] = None