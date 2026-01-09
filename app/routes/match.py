from fastapi import APIRouter, UploadFile, File, Form, HTTPException
import pdfplumber

from app.schemas.match_response import MatchResponse
from app.services.resume_parser import extract_skills
from app.services.jd_matcher import analyze_jd_vs_resume

router = APIRouter(prefix="", tags=["Match"])


@router.post("/match", response_model=MatchResponse)
async def match_resume(
    jd: str = Form(...),
    resume: UploadFile = File(...)
):
    if not jd.strip():
        raise HTTPException(status_code=400, detail="Job description cannot be empty")
    
    if resume.size > 2_000_000:
        raise HTTPException(413, "Resume too large")


    if resume.content_type not in ["application/pdf"]:
        raise HTTPException(status_code=400, detail="Only PDF resumes allowed")

    try:
        text = ""
        with pdfplumber.open(resume.file) as pdf:
            for page in pdf.pages:
                extracted = page.extract_text()
                if extracted:
                    text += extracted
    except Exception:
        raise HTTPException(status_code=500, detail="Failed to read resume PDF")
    

    if not text.strip():
        text = "" #allow empty text, let skill extraction decide

    resume_skills = extract_skills(text)

    if not resume_skills:
        resume_skills = []

    analysis = analyze_jd_vs_resume(
    resume_skills=resume_skills,
    resume_text=text,
    jd_text=jd
)

    return MatchResponse(
    semantic_score=analysis["semantic_score"],
    skill_match_score=analysis["skill_match_score"],
    final_score=analysis["final_score"],
    verdict=analysis["verdict"],
    matched_skills=analysis["matched_skills"],
    missing_skills=analysis["missing_skills"],
    jd_skills=analysis["jd_skills"]
)
