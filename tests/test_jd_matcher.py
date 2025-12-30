from app.services.jd_matcher import analyze_jd_vs_resume, calculate_score

def test_analyze_jd_vs_resume_basic():
    resume_skills = ["Python", "Git", "Docker"]
    jd = "Looking for a Python developer with Docker and AWS experience"

    result = analyze_jd_vs_resume(resume_skills, jd)

    assert "python" in result["matched"]
    assert "docker" in result["matched"]
    assert "aws" in result["missing"]
    assert "git" not in result["jd_skills"]


def test_calculate_score():
    matched = ["python", "docker"]
    jd_skills = ["python", "docker", "aws"]

    score = calculate_score(matched, jd_skills)

    assert score == 66
