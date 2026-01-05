def test_realistic_resume_text():
    text = """
    Experienced Python developer with hands-on Docker,
    AWS, FastAPI and CI/CD pipelines. Strong Git and Linux skills.
    """

    skills = extract_skills(text)

    assert "python" in skills
    assert "docker" in skills
    assert "aws" in skills
    assert "fastapi" in skills
    assert "ci/cd" in skills
    assert "git" in skills