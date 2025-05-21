from fastapi import FastAPI
from api.routes import upload, stats

app = FastAPI(title="Medalist API")

app.include_router(upload.router)
app.include_router(stats.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Medalist API"}
