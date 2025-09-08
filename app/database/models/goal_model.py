from sqlalchemy import Column, Integer, String, ForeignKey, Float, Table
from sqlalchemy.orm import relationship
from app.db import Base
from .association import GoalMember

class Goal(Base):

  """ 
  Table 'Goal' to store goal information
  """

  __tablename__ = "goals"

  id = Column(Integer, primary_key=True, index=True)
  title = Column(String, nullable=False)
  target = Column(Float, nullable=False)
  current_target = Column(Float, default=0)
  description = Column(String, nullable=True)

  # Relasi ke User (many-to-many)
  members = relationship("GoalMember", back_populates="goal", cascade="all, delete-orphan")