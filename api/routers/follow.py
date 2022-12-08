from fastapi import APIRouter, Body, Depends, Header, HTTPException
from fastapi.responses import JSONResponse
from settings import JWT_SECRET_KEY
from sqlalchemy.orm import Session
from database.models import Users, FollowingActivities
from database.db import get_db
from uuid import UUID
from database.serializers import UserSchema, FollowingActivities
from time import perf_counter
import jwt
import uuid
router = APIRouter()

@router.post("/follow/{user_id}")
async def follow_user(access_token: str = Header(None), user_id: UUID = None, SESSION: Session = Depends(get_db)):
    try:
        start_time = perf_counter()
        token = jwt.decode(access_token, JWT_SECRET_KEY, algorithms=["HS256"])
        if token:
            user = SESSION.query(Users).filter(Users.email == token["email"]).one_or_none()
            other_user = SESSION.query(Users).filter(Users.id == user_id).one_or_none()
            user_obj = UserSchema().dump(user)
            other_user_obj = UserSchema().dump(other_user)
            if user_obj.get("id") == other_user_obj.get("id"):
                print(f"API took: {round(perf_counter() - start_time, 2)} secs")
                return JSONResponse(status_code=400, content={"message": "You cannot follow yourself"})
            existing_record = SESSION.query(FollowingActivities).filter(FollowingActivities.user_id == user_obj.get("id"), FollowingActivities.other_user_id == other_user_obj.get("id"), FollowingActivities.type == "following").one_or_none()
            if existing_record:
                print(f"API took: {round(perf_counter() - start_time, 2)} secs")
                return JSONResponse(status_code=400, content={"message": "You are already following this user"})
            following_activity = FollowingActivities(id=uuid.uuid4(),user_id=user_obj.get("id"), type="following", other_user_id=other_user_obj.get("id"))
            SESSION.add(following_activity)
            SESSION.commit()
            SESSION.close()
            print(f"API took: {round(perf_counter() - start_time, 2)} secs")
            return JSONResponse(status_code=200, content={"message": f"You are now following user {other_user_obj.get('username')}"})
        else:
            print(f"API took: {round(perf_counter() - start_time, 2)} secs")
            return JSONResponse(status_code=401, content={"message": "Invalid token"})
    except Exception as e:
        SESSION.rollback()
        SESSION.close()
        return JSONResponse(status_code=500, content={"message": str(e)})

@router.post("/unfollow/{user_id}")
async def unfollow_user(access_token: str = Header(None), user_id: UUID = None, SESSION: Session = Depends(get_db)):
    try:
        start_time = perf_counter()
        token = jwt.decode(access_token, JWT_SECRET_KEY, algorithms=["HS256"])
        if token:
            user = SESSION.query(Users).filter(Users.email == token["email"]).one_or_none()
            other_user = SESSION.query(Users).filter(Users.id == user_id).one_or_none()
            user_obj = UserSchema().dump(user)
            other_user_obj = UserSchema().dump(other_user)
            if user_obj.get("id") == other_user_obj.get("id"):
                print(f"API took: {round(perf_counter() - start_time, 2)} secs")
                return JSONResponse(status_code=400, content={"message": "You cannot unfollow yourself"})
            following_activity = SESSION.query(FollowingActivities).filter(FollowingActivities.user_id == user_obj.get("id"), FollowingActivities.type == "following", FollowingActivities.other_user_id == other_user_obj.get("id")).one_or_none()
            if not following_activity:
                print(f"API took: {round(perf_counter() - start_time, 2)} secs")
                return JSONResponse(status_code=400, content={"message": "You are not following this user"})
            SESSION.delete(following_activity)
            SESSION.commit()
            SESSION.close()
            print(f"API took: {round(perf_counter() - start_time, 2)} secs")
            return JSONResponse(status_code=200, content={"message": f"You are now unfollowing user {other_user_obj.get('username')}"})
        else:
            print(f"API took: {round(perf_counter() - start_time, 2)} secs")
            return JSONResponse(status_code=401, content={"message": "Invalid token"})
    except Exception as e:
        SESSION.rollback()
        SESSION.close()
        return JSONResponse(status_code=500, content={"message": str(e)})