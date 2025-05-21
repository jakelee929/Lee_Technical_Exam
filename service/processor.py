import shutil
import os
from utils.csv_parser import parse_csv
from db import insert_medalists

ARCHIVE_DIR = "storage/app/archive"

def process_file(file_path):
    data = parse_csv(file_path)
    insert_medalists(data)

    os.makedirs(ARCHIVE_DIR, exist_ok=True)
    shutil.move(file_path, os.path.join(ARCHIVE_DIR, os.path.basename(file_path)))
