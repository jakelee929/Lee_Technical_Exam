from fastapi import APIRouter, UploadFile, File, HTTPException
import shutil
import os

router = APIRouter()

UPLOAD_DIR = "storage/app/medalists"

@router.post("/upload")
async def upload_csv(file: UploadFile = File(...)):
    if not file.filename.endswith(".csv"):
        raise HTTPException(status_code=400, detail="Invalid file type")

    os.makedirs(UPLOAD_DIR, exist_ok=True)
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as f:
        shutil.copyfileobj(file.file, f)

    return {"message": "File uploaded successfully", "filename": file.filename}
