from fastapi import FastAPI
from views import UserView, LocationView
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Social Proximity API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or replace with specific domains for security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include the routers
app.include_router(UserView.router)
app.include_router(LocationView.router)

@app.get("/")
async def root():
    """Health check endpoint for the API root"""
    return {"message": "Social Proximity API is running", "status": "ok"}