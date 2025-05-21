from fastapi import FastAPI
from api.routes.upload import medalist
app = FastAPI()
app.include_router(medalist)