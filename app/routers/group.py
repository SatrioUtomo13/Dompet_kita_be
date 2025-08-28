from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.group import GroupCreate, ContributionCreate
from app.database.models.group_model import Group, Contribution
from app.database.models.user_model import User
from app.db import get_db

router = APIRouter(prefix="/groups", tags=["Groups"])

@router.post("/")
def create_group(group: GroupCreate, db: Session = Depends(get_db)):
    """ 
    Create a new group for shared saving.
    """

    db_group = Group(
        name=group.name,
        description=group.description
    )
    db.add(db_group)
    db.commit()
    db.refresh(db_group)
    return db_group

@router.post("/{group_id}/contribute")
def contribute(group_id: int, data: ContributionCreate, db: Session = Depends(get_db)):
    """ 
    Add a user's contribution to a group 
    """
    db_group = db.query(Group).filter(Group.id == group_id).first()
    if not db_group:
        raise HTTPException(status_code=404, detail="Group not found")
    
    db_user = db.query(User).filter(User.id == data.user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    
    db_contribution = Contribution(
        group_id=group_id,
        user_id=data.user_id,
        amount=data.amount,
        role=data.role,
        note=data.note
    )
    db.add(db_contribution)
    db.commit()
    db.refresh(db_contribution)
    return {"message": "Contribution added", "data": db_contribution}