from fastapi import APIRouter, HTTPException
from app.models.expense import ExpenseCreate

router = APIRouter(prefix="/expenses", tags=["Expenses"])

expenses = []

@router.post("/")
def record_expense(data: ExpenseCreate):
    """ 
    Record a shared expense by a user
    """

    expense = {
        "user_id": data.user_id,
        "group_id": data.group_id,
        "amount": data.amount,
        "category": data.category,
        "note": data.note
    }
    expenses.append(expense)
    return {"message": "Expense recorded", "data": expense}