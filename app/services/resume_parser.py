import re

COMMON_SKILLS = [
    "python", "java", "sql", "excel", "react", "node",
    "fastapi", "django", "aws", "git", "docker"
]

def extract_skills(text: str):
    text_lower = text.lower()
    found = []
    for skill in COMMON_SKILLS:
        if skill in text_lower:
            found.append(skill.capitalize())
    return list(set(found))


def extract_education(text: str):
    match = re.search(r"(bachelor|b\.sc|bcs|master|m\.sc)", text.lower())
    return match.group(0).upper() if match else "Not found"


def extract_experience(text: str):
    match = re.search(r"(\d+)\+?\s+years?", text.lower())
    return match.group(1) if match else "0"

from fastapi import APIRouter, UploadFile, File, HTTPException
import pdfplumber

router = APIRouter(prefix="/resume", tags=["Resume"])

@router.post("/upload")
async def upload_resume(file: UploadFile = File(...)):
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Only PDF files allowed")

    try:
        text = ""
        with pdfplumber.open(file.file) as pdf:
            for page in pdf.pages:
                extracted = page.extract_text()
                if extracted:
                    text += extracted

        if not text.strip():
            raise HTTPException(
                status_code=422,
                detail="No readable text found in PDF"
            )

        return {
            "filename": file.filename,
            "text_preview": text[:500]
        }

        
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to process PDF: {str(e)}"
        )

