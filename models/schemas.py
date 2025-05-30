from pydantic import BaseModel
from typing import List, Optional

class Document(BaseModel):
    type: str
    hospital_name: Optional[str] = None
    total_amount: Optional[float] = None
    date_of_service: Optional[str] = None
    patient_name: Optional[str] = None
    diagnosis: Optional[str] = None
    admission_date: Optional[str] = None
    discharge_date: Optional[str] = None

class Validation(BaseModel):
    missing_documents: List[str]
    discrepancies: List[str]
    claim_decision: dict

class ClaimResponse(BaseModel):
    documents: List[Document]
    validation: Validation