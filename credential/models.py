""" DATABASE models, used from SQLAlchemy """

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base


class Credential(Base):
    __tablename__ = 'credentials'
    id = Column(Integer, primary_key=True, index=True)
    service_name = Column(String)
    password = Column(String) 
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates='credentials')


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    surname = Column(String)
    password = Column(String)
    backup_password = Column(String)
    credentials = relationship('Credential', back_populates='user')
