from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from . import model

def get_challenge_quota(db: Session, user_id: str):
    return(db.query(model.ChallengeQuota).filter(model.ChallengeQuota.user_id == user_id).first())

def create_challenge_quota(db: Session, user_id: str):
    db_quota = model.ChallengeQuota(user_id = user_id)
    db.add(db_quota)
    db.commit()
    db.refresh(db_quota)
    return db_quota

def reset_quta_if_needed(db: Session, quota: model.ChallengeQuota):
    now = datetime.now()
    if now - quota.last_reset_date > timedelta(hours = 24):
        quota.remaining_quota = 10
        quota.last_reset_date = now
        db.commit()
        db.refresh(quota)
    return quota

def create_challenge(
    db: Session,
    difficulty: str,
    created_by: str,
    title: str,
    options: str,
    correct_answer_id: int,
    explanation: str
):
    db_challenge = model.Challenge(
        difficulty = difficulty,
        created_by = created_by,
        title = title,
        options = options,
        correct_answer_id = correct_answer_id,
        explanation = explanation
    )
    db.add(db_challenge)
    db.commit()
    db.refresh(db_challenge)
    return db_challenge

def get_user_challenges(db: Session, user_id: str):
    return db.query(model.Challenge).filter(model.Challenge.created_by == user_id).all()