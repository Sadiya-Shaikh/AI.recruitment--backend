from fastapi import FastAPI
from app.routes.health import router as health_router
from app.routes.resume import router as resume_router 

app = FastAPI(title="AI Recruitment System")

app.include_router(health_router)
app.include_router(resume_router)
@app.get("/")
def root():
    return {"message": "Backend is running"}
