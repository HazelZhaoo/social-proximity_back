from sqlalchemy.ext.declarative import declarative_base
from motor.motor_asyncio import AsyncIOMotorClient

# Keep declarative_base for models
Base = declarative_base()

# MongoDB Config
MONGO_URI = "mongodb+srv://danielbaker06072001:GenAI2025Team@genai2025.tjoog.mongodb.net/?retryWrites=true&w=majority&appName=genai2025"
mongo_client = AsyncIOMotorClient(MONGO_URI)
mongodb = mongo_client["genai"]

# Remove the empty get_db function since we're not using PostgreSQL
# Dependency for MongoDB
async def get_mongo_db():
    yield mongodb