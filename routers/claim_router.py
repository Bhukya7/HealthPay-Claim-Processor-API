from fastapi import APIRouter, UploadFile, File
from typing import List
from app.orchestration.workflow import process_claim

router = APIRouter(prefix="/api/v1", tags=["claims"])

@router.post("/process-claim", summary="Process uploaded claim documents")
async def process_claim_endpoint(files: List[UploadFile] = File(...)):
    """
    Processes uploaded PDF documents (e.g., bill, discharge summary) and returns extracted data and validation results.
    """
    return await process_claim(files)