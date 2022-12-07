from fastapi import APIRouter, Body, Depends, Header, HTTPException


router = APIRouter()

@router.get("/comments")
async def get_user():
    return {"message": "Hello World"}