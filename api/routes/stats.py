from fastapi import APIRouter, Query
from typing import Optional
from service.db import get_aggregated_event_stats

router = APIRouter()

@router.get("/aggregated_stats/event")
async def get_event_stats(page: int = Query(1, gt=0)):
    return get_aggregated_event_stats(page)
