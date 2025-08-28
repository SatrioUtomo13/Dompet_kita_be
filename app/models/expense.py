from pydantic import BaseModel
from typing import Optional

# Expense creation schema
class ExpenseCreate(BaseModel):
    user_id: int
    group_id: int
    amount: float
    category: str
    note: Optional[str] = None