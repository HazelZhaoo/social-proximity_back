from fastapi import APIRouter, HTTPException, Depends, status
from models.Database import get_mongo_db
from motor.motor_asyncio import AsyncIOMotorDatabase
from models.Common import CommonResponse

router = APIRouter(prefix="/api")

@router.get("/health-check")
async def health_check():
    return {"status": "ok"}

@router.post("/save-gps")
async def save_gps(
    location_data: dict,  # Add a request body
    mongo_db: AsyncIOMotorDatabase = Depends(get_mongo_db),
):
    try:
        # Actually save the data to MongoDB
        result = await mongo_db["location"].insert_one(location_data)
        
        if not result.inserted_id:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Failed to save GPS data"
            )
            
        return {
            "status": "success",
            "message": "GPS Data Saved",
            "location_id": str(result.inserted_id)
        }
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )