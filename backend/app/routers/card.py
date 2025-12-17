from fastapi import APIRouter
import uuid

router = APIRouter()

@router.post("/create")
def create_card(data: dict):
    slug = f"{data['full_name'].lower()}-{uuid.uuid4().hex[:6]}"
    return {"slug": slug}

