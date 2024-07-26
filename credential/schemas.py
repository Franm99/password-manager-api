""" DATA models, used from FastAPI """
from credential.models import Credential
from pydantic import BaseModel
from typing import Optional


class Credential(BaseModel):
    service_name: str 
    password: str 
    user_id: int


class User(BaseModel):
    name: str 
    surname: str
    password: str 
    backup_password: str


class Login(BaseModel):
    user: str 
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str 


class TokenData(BaseModel):
    user: Optional[str] = None

class DisplayUser(BaseModel):
    name: str
    surname: str


class DisplayCredential(BaseModel):
    service_name: str 
    user: DisplayUser
    
    class Config:
        orm_mode = True 
