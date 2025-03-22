from fastapi import FastAPI
from views import UserView

app = FastAPI()
app.include_router(UserView.router)
