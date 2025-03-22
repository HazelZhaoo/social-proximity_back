from motor.motor_asyncio import AsyncIOMotorDatabase

async def save_location(
    location_data: dict,
    mongo_db: AsyncIOMotorDatabase,
): 
    """
    Save location data to MongoDB
    
    Args:
        location_data: Dictionary containing location information
        mongo_db: MongoDB connection
        
    Returns:
        The inserted location ID
    """
    result = await mongo_db["location"].insert_one(location_data)
    return str(result.inserted_id)