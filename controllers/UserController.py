from models.UserModel import UserModel
from motor.motor_asyncio import AsyncIOMotorDatabase

async def get_all_users(mongo_db: AsyncIOMotorDatabase):
    # Removed the db parameter since it's not being used
    mongo_users_cursor = mongo_db["user"].find()
    mongo_users = []
    async for user in mongo_users_cursor:
        user["_id"] = str(user["_id"])
        mongo_users.append(user)

    return {
        "mongo_users": mongo_users,
    }