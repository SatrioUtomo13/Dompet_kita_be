from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from app.db import Base
from .association import goal_members

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
  goals = relationship("Goal", secondary=goal_members, back_populates="members")