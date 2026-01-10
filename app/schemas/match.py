from pydantic import BaseModel
from typing import List

class JDInput(BaseModel):
    job_description: str


class MatchResponse(BaseModel):
    semantic_score: float
    skill_match_score: float
    final_score: float
    verdict: str
    matched_skills: List[str]
    missing_skills: List[str]
    jd_skills: List[str]
