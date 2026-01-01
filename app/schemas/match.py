from pydantic import BaseModel
from typing import List

class MatchResponse(BaseModel):
  match_score: int
  matched_skills: List[str]
  missing_skills: List[str]
  jd_skills: List[str]
