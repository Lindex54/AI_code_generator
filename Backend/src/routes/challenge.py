from fastapi import APIRouter, Depends, HTTPException, Request
from pydantic import BaseModel
from sqlalchemy.orm import Session
from ..database.db import(
    get_challenge_quota,
    create_challenge,
    create_challenge_quota,
    reset_quta_if_needed,
    get_user_challenges
)
from ..utils import authenticate_and_get_user_details
from ..database.model import get_db
import json
from datetime import datetime

router = APIRouter()

class ChallengeRequest(BaseModel):
    difficulty: str
    
    class Confiq:
        json_schema_extra = {"example": {"difficulty": "easy"}}
   
@router.post("/generate-challenge")
async def generate_challenge(request: ChallengeRequest, db: Session = Depends(get_db)):
    try:
        user_details = authenticate_and_get_user_details(request)
        user_id = user_details.get("user_id")
        
        quota = get_challenge_quota(db, user_id)
        if not quota:
            create_challenge_quota(db, user_id)
        
        quota = reset_quta_if_needed(db, quota)
    except Exception as e:
        pass
    

@router.get("/my-history")
async def my_history(request: Request, db:Session = Depends(get_db)):
    user_details = authenticate_and_get_user_details(request)
    user_id = user_details.get("user_id")

    challenges = get_user_challenges(db, user_id)
    return {"challenges": challenges}

@router.get("/guota")
async def get_quota(request: Request, db: Session = Depends(get_db)):
    user_details = authenticate_and_get_user_details(request)
    user_id = user_details.get("user_id")
    
    quota = get_challenge_quota(db, user_id)
    if not quota:
        return {
            "user_id": user_id,
            "quota_remaining": 0,
            "last_reset_date": datetime.now()
        }
    quota = reset_quta_if_needed(db, quota)
    return quota