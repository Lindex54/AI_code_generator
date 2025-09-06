from fastapi import APIRouter, Depends, HTTPException, Request
from pydantic import BaseModel
from sqlalchemy.orm import Session
from ..ai_generator import generate_challenge_with_ai
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
        
        if quota.remaining_quota <= 0:
            raise HTTPException(status_code=429, detail="Daily challenge quota exceeded")
        
        challenge_data = generate_challenge_with_ai(request.difficulty)

        new_challenge = create_challenge(
            db = db,
            difficulty = request.difficulty,
            created_by = user_id,
            **challenge_data
            # title = challenge_data.get("title"),
            # options = json.dumps(challenge_data.get("options")),
            # correct_answer_id = challenge_data.get("correct_answer_id"),
            # explanation = challenge_data.get("explanation")
        )
        
        quota.remaining_quota -= 1
        db.commit()
        return {
            "id": new_challenge.id,
            "title": new_challenge.title,
            "options": json.loads(new_challenge.options),
            "correct_answer_id": new_challenge.correct_answer_id,
            "explanation": new_challenge.explanation,
            "timestamp": new_challenge.date_create.isoformat()
        }
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    

@router.get("/my-history")
async def my_history(request: Request, db:Session = Depends(get_db)):
    user_details = authenticate_and_get_user_details(request)
    user_id = user_details.get("user_id")

    challenges = get_user_challenges(db, user_id)
    return {"challenges": challenges}

@router.get("/quota")
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