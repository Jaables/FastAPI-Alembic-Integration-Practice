import sys

from typing import Optional
from fastapi import Depends, APIRouter
import models
from database import engine, SessionLocal
from pydantic import BaseModel
from .auth import get_current_user, get_user_exception

sys.path.append("..")

router = APIRouter(
    prefix="/address",
    tags=["address"],
    responses={404: {"description": "Not found"}}
)

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

class Address(BaseModel):
    address1: str
    address2: Optional[str]
    city: str
    state: str
    country: str
    postcode: str