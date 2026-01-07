from pydantic import BaseModel
from typing import List

class MatchResponse(BaseModel):
    semantic_score: int
    skill_match_score: int
    final_score: int
    matched_skills: list[str]
    missing_skills: list[str]
    jd_skills: list[str]
