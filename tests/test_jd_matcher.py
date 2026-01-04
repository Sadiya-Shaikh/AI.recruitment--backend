from app.services.jd_matcher import analyze_jd_vs_resume, calculate_score

def test_analyze_jd_vs_resume_basic():
    resume_skills = ["Python", "Git", "Docker"]
    jd = "Looking for a Python developer with Docker and AWS experience"

    result = analyze_jd_vs_resume(resume_skills, jd)

    assert "python" in result["matched_skills"]
    assert "docker" in result["matched_skills"]
    assert "aws" in result["missing_skills"]
    assert "git" not in result["jd_skills"]



def test_score_is_jd_based():
    matched_skills = ["python", "git"]
    jd_skills = ["python", "git", "docker", "aws"]

    score = calculate_score(matched_skills, jd_skills)

    assert score == 50
