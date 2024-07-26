from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi.params import Depends
from fastapi import Response, HTTPException
from fastapi import status
from ..database import get_db
from .. import models
from .. import schemas
from typing import List
from credential.routers.login import get_current_user


router = APIRouter(
    tags=["Credentials"],
    prefix="/credential"
    
)

@router.delete('/{id}')
def delete(id, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    db.query(models.Credential).filter(models.Credential.id == id).delete(synchronize_session=False)
    db.commit()
    return {f"Credential with id={id} deleted"}


@router.get('/', response_model=List[schemas.DisplayCredential])
def credentials(db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    credentials = db.query(models.Credential).all()
    return credentials


@router.get('/{id}', response_model=schemas.DisplayCredential)
def credential(id, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    credential = db.query(models.Credential).filter(models.Credential.id == id).first()
    if not credential:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Credential not found')
    return credential


@router.put('/{id}')
def update(id, request: schemas.Credential, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    credential = db.query(models.Credential).filter(models.Credential.id == id)
    if not credential.first():
        pass
    credential.update(request.dict())
    db.commit()
    return {f'Credential with id="{id}" updated'}



@router.post('/', status_code=status.HTTP_201_CREATED)
def add(
    request: schemas.Credential, 
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(get_current_user)
    ):
    new_credential = models.Credential(
        service_name=request.service_name, 
        password=request.password,
        user_id=request.user_id
    )
    db.add(new_credential)
    db.commit()
    db.refresh(new_credential)

    return request