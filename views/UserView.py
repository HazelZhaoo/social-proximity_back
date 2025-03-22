from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from controllers.UserController import get_all_users
from models.Database import get_db, get_mongo_db
from motor.motor_asyncio import AsyncIOMotorDatabase
from models.UserModel import UserCreateRequest, UserCreateResponse
from models.Common import CommonResponse

router = APIRouter()


@router.get("/users")
async def get_all(
    # db: Session = Depends(get_db),
    mongo_db: AsyncIOMotorDatabase = Depends(get_mongo_db),
):
    return await get_all_users(db, mongo_db)


@router.post("/users")
async def create_user(
    user: UserCreateRequest,
    # db: Session = Depends(get_db),
    mongo_db: AsyncIOMotorDatabase = Depends(get_mongo_db),
):
    print(user)
    # Saving Username, email and unique user_id
    result = await mongo_db["user"].insert_one(
        {"username": user.username, "email": user.email}
    )

    # ! error
    if not result.inserted_id:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="failed to create user",
        )

    userCreateResponse = UserCreateResponse(
        user_id=str(result.inserted_id), username=user.username, email=user.email
    )

    return CommonResponse[UserCreateResponse](
        Status="Success",
        ErrorMessage="",
        Data=[userCreateResponse],  # Optional: You may want a response model for this
    )
