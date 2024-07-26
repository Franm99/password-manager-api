from fastapi import FastAPI, HTTPException
from fastapi.params import Depends
from fastapi import status
from sqlalchemy.orm import Session
from typing import List
from . import schemas 
from . import models
from .database import engine, SessionLocal, get_db
from .routers import credentials, users, login

app = FastAPI(
    title="Password Manager API",
    description="Manage your passwords easily from this simple API.",
    terms_of_service="https://franm99.github.io/portfolio-fr/",
    contact={
        "Developer name": "Francisco Moreno",
        "website": "https://franm99.github.io/portfolio-fr/",
        "email": "fran.moreno.se@gmail.com",
    },
    license_info={
        "name": "XYZ",
        "url": "http://www.google.com",
    },
    redoc_url=None,
)

app.include_router(credentials.router)
app.include_router(users.router)
app.include_router(login.router)

models.Base.metadata.create_all(engine)







