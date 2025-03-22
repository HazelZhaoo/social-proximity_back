from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from motor.motor_asyncio import AsyncIOMotorClient

# PostgreSQL Config
# DATABASE_URL = "postgresql://postgres:Cel-365.@localhost:5432/postgres"

# engine = create_engine(DATABASE_URL)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# MongoDB Config
MONGO_URI = "mongodb+srv://danielbaker06072001:GenAI2025Team@genai2025.tjoog.mongodb.net/?retryWrites=true&w=majority&appName=genai2025"
mongo_client = AsyncIOMotorClient(MONGO_URI)
mongodb = mongo_client["genai"]


def get_db():
    return


#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


# Dependency for MongoDB
async def get_mongo_db():
    yield mongodb
