from pydantic import BaseModel
from typing import List

class MatchResponse(BaseModel):
    jd_skills: List[str]
    matched_skills: List[str]
    missing_skills: List[str]
    match_score: int
