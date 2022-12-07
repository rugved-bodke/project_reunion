from fastapi import APIRouter, Body, Depends, Header, HTTPException


router = APIRouter()

@router.get("/user")
async def get_user():
    return {"message": "Hello World"}