from fastapi import APIRouter, UploadFile, File, Form, HTTPException
import pdfplumber

from app.services.resume_parser import extract_skills
from app.services.jd_matcher import match_skills, calculate_score

router = APIRouter(prefix="/match", tags=["Match"])

@router.post("/")
async def match_resume(
    jd: str = Form(...),
    resume: UploadFile = File(...)
):
    # 1️⃣ Validate JD
    if not jd.strip():
        raise HTTPException(status_code=400, detail="Job description cannot be empty")

    # 2️⃣ Validate file type
    if resume.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Only PDF resumes allowed")

    # 3️⃣ Extract resume text safely
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

    # 4️⃣ Extract resume skills
    resume_skills = extract_skills(text)

    if not resume_skills:
        raise HTTPException(
            status_code=422,
            detail="No skills detected in resume"
        )

    # 5️⃣ Match against JD
    matched, missing = match_skills(resume_skills, jd)
    score = calculate_score(matched, missing)

    return {
        "match_score": score,
        "matched_skills": matched,
        "missing_skills": missing
    }
