from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from app.db import Base

class Group(Base):

    """ 
    Table 'Group' to store group information
    """

    __tablename__ = "groups"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)

    contributions = relationship("Contribution", back_populates="group")

class Contribution(Base):

    """ 
    Table 'contribution to store user contributions to groups
    """

    __tablename__ = 'contributions'

    id = Column(Integer, primary_key=True, index=True)
    group_id = Column(Integer, ForeignKey('groups.id'))
    user_id = Column(Integer)
    amount = Column(Float)
    role = Column(String, nullable=False)
    note = Column(String, nullable=True)

    group = relationship("Group", back_populates="contributions")