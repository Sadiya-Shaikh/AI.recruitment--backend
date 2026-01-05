def test_skill_aliases():
    text = "Experienced in Python3 and Docker Compose"
    skills = normalize_skills(text)

    assert "python" in skills
    assert "docker" in skills
