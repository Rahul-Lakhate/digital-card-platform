from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_templates():
    return [
        {"id": 1, "name": "Minimal"},
        {"id": 2, "name": "Creative"},
        {"id": 3, "name": "Professional"}
    ]

