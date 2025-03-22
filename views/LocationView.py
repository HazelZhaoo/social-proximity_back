from fastapi import APIRouter, HTTPException, Depends, status
from models.Database import get_db, get_mongo_db
from motor.motor_asyncio import AsyncIOMotorDatabase
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/health-check")
async def health_check():
    return {"status": "ok"}


@router.post("/save-gps")
async def save_gps(
    # db: Session = Depends(get_db),
    mongo_db: AsyncIOMotorDatabase = Depends(get_mongo_db),
):
    print("GPS Data Saved")
    return
