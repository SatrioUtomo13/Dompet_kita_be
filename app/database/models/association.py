from sqlalchemy import Column, Integer, String, Float, ForeignKey, Table
from app.db import Base

goal_members = Table(
  "goal_members",
  Base.metadata,
  Column("goal_id", Integer, ForeignKey("goals.id", ondelete="CASCADE"), primary_key=True),
  Column("user_id", Integer, ForeignKey("users.id", ondelete="CASCADE"), primary_key=True)
)