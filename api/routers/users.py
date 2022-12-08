from fastapi import APIRouter, Body, Depends, Header, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Dict, List, Literal, Optional, Union
from database.db import get_db
from database.models import Users
from sqlalchemy.orm import Session
from settings import JWT_SECRET_KEY
from database.serializers import UserSchema
from time import perf_counter
import jwt


router = APIRouter()

@router.get("/user")
async def get_user(access_token: str = Header(None), SESSION: Session = Depends(get_db)):
    try:
        start_time = perf_counter()
        user = jwt.decode(access_token, JWT_SECRET_KEY, algorithms=["HS256"])
        email = user["email"]
        user = SESSION.query(Users).filter(Users.email == email).one_or_none()
        if not user:
            return JSONResponse(status_code=401, content={"message": "Invalid token"})
        user_obj = UserSchema().dump(user)
        data = {
            "username": user_obj["username"],
            "number_of_followers": "followers",
            "number_of_following": "following",
        }
        print(f"API took: {round(perf_counter() - start_time, 2)} secs")
        return JSONResponse(status_code=200, content=data)
    except Exception as e:
        return JSONResponse(status_code=500, content={"message": str(e)})