from fastapi import APIRouter, Body, Depends, Header, HTTPException
from pydantic import BaseModel
from typing import Dict, List, Literal, Optional, Union
from database.db import get_db
from database.models import Users
from sqlalchemy.orm import Session
from settings import FERNET_SECRET_KEY, JWT_SECRET_KEY
from database.serializers import UserSchema
from fastapi.responses import JSONResponse
from cryptography.fernet import Fernet
from time import perf_counter
import jwt

pwd_context = Fernet(FERNET_SECRET_KEY)

def encode(plaintext):
    code = plaintext.encode('utf-8')
    encoded_text = pwd_context.encrypt(code)
    passcode_hash = encoded_text.decode('utf-8')
    return passcode_hash

def decode(hashed_text):
    code = hashed_text.encode('utf-8')
    encoded_text = pwd_context.decrypt(code)
    passcode = encoded_text.decode('utf-8')
    return passcode


class AuthUser(BaseModel):
    email: str
    password: str


router = APIRouter()


@router.post("/auth")
async def auth_user(args: AuthUser, SESSION: Session = Depends(get_db)):
    try:
        start_time = perf_counter()
        email = args.email
        password = args.password
        user = SESSION.query(Users).filter(Users.email == email).one_or_none()
        if not user:
            print(f"API took: {round(perf_counter() - start_time, 2)} secs")
            return JSONResponse(status_code=404, content={"message": "User not found"})
        user_obj = UserSchema().dump(user)
        hashed_password = user_obj["password"]
        if decode(hashed_password) == password:
            token = jwt.encode({"email": email, "password": args.password}, JWT_SECRET_KEY, algorithm="HS256")
            print(f"API took: {round(perf_counter() - start_time, 2)} secs")
            return JSONResponse(status_code=200, content={"token": token})
        else:
            print(f"API took: {round(perf_counter() - start_time, 2)} secs")
            return JSONResponse(status_code=401, content={"message": "Invalid password"})
    except Exception as e:
        return JSONResponse(status_code=500, content={"message": str(e)})