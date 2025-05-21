from pydantic import BaseModel
from typing import Optional
from datetime import date

class Medalist(BaseModel):
    discipline: str
    event: str
    event_gender: Optional[str] = None
    event_date: Optional[date] = None
    name: str
    medal_type: str
    gender: Optional[str] = None
    country: str
    country_code: str
    nationality: str
    medal_code: str
    medal_date: Optional[date] = None
