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
