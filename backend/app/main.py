from fastapi import FastAPI
from app.routers import auth, payment, card, template

app = FastAPI(title="Digital Card Platform API")

app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(payment.router, prefix="/payment", tags=["Payment"])
app.include_router(card.router, prefix="/card", tags=["Card"])
app.include_router(template.router, prefix="/template", tags=["Template"])

@app.get("/")
def health():
    return {"status": "ok"}
