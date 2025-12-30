from fastapi import APIRouter, UploadFile, File, HTTPException
import pdfplumber
import logging

logger = logging.getLogger(__name__)

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
        from app.services.resume_parser import (
        extract_skills,
        extract_education,
        extract_experience
         )
        
        
      
        return {
    "filename": file.filename,
    "parsed": True,
    "data": {
        "skills": extract_skills(text),
        "education": extract_education(text),
        "experience_years": extract_experience(text)
    }
}


    except HTTPException:
     raise
    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Internal server error while processing resume"
        )

    except Exception as e:
     logger.exception("Resume processing failed")
    raise HTTPException(status_code=500, detail="Internal server error")

    skills = extract_skills(text)

    if not skills:
     return {
        "filename": file.filename,
        "parsed": False,
        "error": "Unable to extract skills from resume"
    }
