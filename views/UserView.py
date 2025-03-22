from fastapi import APIRouter, HTTPException, Depends, status
from controllers.UserController import get_all_users
from models.Database import get_mongo_db
from motor.motor_asyncio import AsyncIOMotorDatabase
from models.UserModel import UserCreateRequest, UserCreateResponse
from models.Common import CommonResponse

router = APIRouter(prefix="/api")

@router.get("/users")
async def get_all(
    mongo_db: AsyncIOMotorDatabase = Depends(get_mongo_db)
):
    # Removed db parameter since it's not being used
    return await get_all_users(mongo_db)

@router.post("/users")
async def create_user(
    user: UserCreateRequest,
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
        Data=[userCreateResponse],
    )