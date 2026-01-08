from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

SKILL_WEIGHTS = {
    "python": 2,
    "docker": 2,
    "aws": 3,
    "fastapi": 1,
    "git": 1,
    "linux": 2,
    "ci/cd": 2
}


def weighted_skill_score(matched: list[str], jd_skills: list[str]) -> int:
    if not jd_skills:
        return 0

    total_weight = sum(SKILL_WEIGHTS.get(skill, 1) for skill in jd_skills)
    matched_weight = sum(SKILL_WEIGHTS.get(skill, 1) for skill in matched)

    return round((matched_weight / total_weight) * 100)


def semantic_score(resume_text: str, jd_text: str) -> int:
    if not resume_text.strip() or not jd_text.strip():
        return 0

    vectorizer = TfidfVectorizer()
    tfidf = vectorizer.fit_transform([resume_text, jd_text])
    similarity = cosine_similarity(tfidf[0:1], tfidf[1:2])[0][0]

    return round(similarity * 100)
