from fastapi import APIRouter, UploadFile, File, Form, HTTPException
import pdfplumber

from app.schemas.match import MatchResponse
from app.services.resume_parser import extract_skills
from app.services.jd_matcher import analyze_jd_vs_resume, calculate_score

router = APIRouter(prefix="/match", tags=["Match"])


@router.post("/", response_model=MatchResponse)
async def match_resume(
    jd: str = Form(...),
    resume: UploadFile = File(...)
):
    if not jd.strip():
        raise HTTPException(status_code=400, detail="Job description cannot be empty")

    if resume.content_type != "application/pdf":
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
        raise HTTPException(status_code=422, detail="No readable text found in resume")

    resume_skills = extract_skills(text)
    if not resume_skills:
        raise HTTPException(status_code=422, detail="No skills detected in resume")

    analysis = analyze_jd_vs_resume(resume_skills, jd)

    score = calculate_score(
        analysis["matched_skills"],
        analysis["jd_skills"]
    )

    return {
        "match_score": score,
        "matched_skills": analysis["matched_skills"],
        "missing_skills": analysis["missing_skills"],
        "jd_skills": analysis["jd_skills"]
    }
