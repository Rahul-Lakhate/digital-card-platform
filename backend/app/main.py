from fastapi import FastAPI
from app.routers import payment, card, template

app = FastAPI()

app.include_router(payment.router, prefix="/payment")
app.include_router(card.router, prefix="/card")
app.include_router(template.router, prefix="/template")

@app.get("/")
def root():
    return {"status": "running"}
