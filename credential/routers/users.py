from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi.params import Depends
from fastapi import Response, HTTPException
from fastapi import status
from ..database import get_db
from .. import models
from .. import schemas
from typing import List
from passlib.context import CryptContext


router = APIRouter()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


@router.post('/user', response_model=schemas.DisplayUser, tags=["Users"])
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    hashed_password = pwd_context.hash(request.password)
    hashed_backup_password = pwd_context.hash(request.backup_password)
    new_user = models.User(
        name=request.name,
        surname=request.surname,
        password=hashed_password,
        backup_password=hashed_backup_password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user