# AI Recruitment Backend

A FastAPI-based backend system for parsing resumes, extracting skills, and matching them against job descriptions with explainable scoring.

## Features
- Resume PDF upload and text extraction
- Skill extraction from resumes
- Job Description (JD) skill matching
- Match score calculation with missing skill analysis
- REST APIs with Swagger UI

## Tech Stack
- Python
- FastAPI
- pdfplumber
- Uvicorn

## API Endpoints

### Health Check
GET /health

### Resume Upload
POST /resume/upload  
- Input: PDF file  
- Output: Extracted resume text preview

### JD Matching
POST /match  
- Input:
  - Resume (PDF)
  - Job Description (text)
- Output:
  - Match score
  - Matched skills
  - Missing skills

## How to Run Locally

```bash
git clone https://github.com/Sadiya-Shaikh/AI.recruitment-backend.git
cd AI.recruitment-backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
