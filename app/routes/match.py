from fastapi import APIRouter, UploadFile, File, Form, HTTPException
import pdfplumber
import io 
from io import BytesIO

from app.schemas.match import JDInput, MatchResponse
from app.services.resume_parser import extract_skills
from app.services.jd_matcher import analyze_jd_vs_resume

router = APIRouter(tags=["Match"])

ALLOWED_TYPES = ["application/pdf"]
MAX_FILE_SIZE = 2 * 1024 * 1024  # 2MB


@router.post("/match", response_model=MatchResponse)
async def match_resume(
    jd: str = Form(...),
    resume: UploadFile = File(...)
):
    if not jd.strip():
        raise HTTPException(status_code=400, detail="Job description cannot be empty")
    
    
    if not text.strip():
     raise HTTPException(
            status_code=422,
            detail="Resume contains no readable text (scanned PDF)"
        )
    ALLOWED_TYPES = ["application/pdf"]
    MAX_FILE_SIZE = 2 * 1024 * 1024  # 2MB

    if resume.content_type not in ALLOWED_TYPES:
        raise HTTPException(status_code=415, detail="Only PDF resumes allowed")

    contents = await resume.read()
    if len(contents) > MAX_FILE_SIZE:
        raise HTTPException(status_code=413, detail="Resume too large")

    
    contents = await resume.read()

    try:
      text = ""
      with pdfplumber.open(BytesIO(contents)) as pdf:
        for page in pdf.pages:
            extracted = page.extract_text()
            if extracted:
                text += extracted
    except Exception as e:
       raise HTTPException(status_code=500, detail="Failed to read resume PDF")

    resume_skills = extract_skills(text) if text else []

    analysis = analyze_jd_vs_resume(
        resume_skills=resume_skills,
        resume_text=text,
        jd_text=jd
    )

    return MatchResponse(**analysis)
