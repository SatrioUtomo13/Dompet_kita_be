from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from app.db import Base
from .association import GoalMember

class User(Base):

  """ 
  Table 'users' to store user information
  """

  __tablename__ = "users"

  id = Column(Integer, primary_key=True, index=True)
  name = Column(String, nullable=False)
  email = Column(String, unique=True, nullable=False)
  password = Column(String, nullable=False)

  # Relasi ke Goal (many-to-many)
  goal_members = relationship("GoalMember", back_populates="user", cascade="all, delete-orphan")