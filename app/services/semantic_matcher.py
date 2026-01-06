from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def semantic_match(resume_skills: list[str], jd_skills: list[str]) -> int:
    if not resume_skills or not jd_skills:
        return 0

    resume_text = " ".join(resume_skills)
    jd_text = " ".join(jd_skills)

    vectorizer = TfidfVectorizer()
    tfidf = vectorizer.fit_transform([resume_text, jd_text])

    similarity = cosine_similarity(tfidf[0:1], tfidf[1:2])[0][0]
    return round(similarity * 100)
