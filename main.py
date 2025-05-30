from fastapi import FastAPI
from app.routers.claim_router import router as claim_router

app = FastAPI(
    title="HealthPay Claim Processor",
    description="API for processing healthcare claims by extracting and validating data from uploaded documents.",
    version="1.0.0"
)

app.include_router(claim_router)

@app.get("/", summary="Root endpoint")
async def root():
    """
    Returns a welcome message for the HealthPay Claim Processor API.
    """
    return {"message": "HealthPay Claim Processor API"}