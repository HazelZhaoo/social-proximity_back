from models.UserModel import UserModel
from sqlalchemy.orm import Session
from motor.motor_asyncio import AsyncIOMotorDatabase


async def get_all_users(db: Session, mongo_db: AsyncIOMotorDatabase):

    # pg_users = db.query(UserModel).all()
    mongo_users_cursor = mongo_db["user"].find()
    mongo_users = []
    async for user in mongo_users_cursor:
        user["_id"] = str(user["_id"])
        mongo_users.append(user)

    return {
        # "postgres_users": [u.__dict__ for u in pg_users],
        "mongo_users": mongo_users,
    }
