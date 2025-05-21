import csv
from datetime import datetime

def parse_date(value):
    try:
        return datetime.strptime(value, "%Y-%m-%d").date()
    except:
        return None

def parse_csv(filepath):
    records = []
    with open(filepath, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            records.append({
                "discipline": row.get("discipline"),
                "event": row.get("event"),
                "event_gender": row.get("event_gender"),
                "event_date": parse_date(row.get("event_date")),
                "name": row.get("name"),
                "medal_type": row.get("medal_type"),
                "gender": row.get("gender"),
                "country": row.get("country"),
                "country_code": row.get("country_code"),
                "nationality": row.get("nationality"),
                "medal_code": row.get("medal_code"),
                "medal_date": parse_date(row.get("medal_date")),
            })
    return records
