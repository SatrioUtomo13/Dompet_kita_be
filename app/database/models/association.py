from sqlalchemy import Column, Integer, String, Float, ForeignKey, Table, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db import Base

# goal_members = Table(
#   "goal_members",
#   Base.metadata,
#   Column("goal_id", Integer, ForeignKey("goals.id", ondelete="CASCADE"), primary_key=True),
#   Column("user_id", Integer, ForeignKey("users.id", ondelete="CASCADE"), primary_key=True)
# )

class GoalMember(Base):
  __tablename__ = "goal_members"

  goal_id = Column(Integer, ForeignKey("goals.id", ondelete="CASCADE"), primary_key=True)
  user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), primary_key=True)

  # Additional fields
  role = Column(String, default="member")
  total_contributed = Column(Float, default=0)
  last_activity = Column(DateTime, default=datetime.utcnow)

  # Relationships
  goal = relationship("Goal", back_populates="members")
  user = relationship("User", back_populates="goal_members")