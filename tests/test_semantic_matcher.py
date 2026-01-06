from app.services.semantic_matcher import semantic_match


def test_semantic_similarity_high():
    resume = ["python", "fastapi", "rest api"]
    jd = ["backend services", "python", "api development"]

    score = semantic_match(resume, jd)
    assert score > 40
