from typing import List, Set

from typing import List, Set

def match_skills(resume_skills: List[str], jd_text: str):
    jd_text = jd_text.lower()

    resume_set = {s.lower() for s in resume_skills}
    jd_skills = {s for s in KNOWN_SKILLS if s in jd_text}

    matched = resume_set.intersection(jd_skills)
    missing = jd_skills - resume_set

    return list(matched), list(missing)

KNOWN_SKILLS = {
    "python", "java", "javascript", "react", "node",
    "express", "mongodb", "sql", "git", "github",
    "docker", "aws", "fastapi", "flask",
    "html", "css", "linux"
}


def calculate_score(matched: List[str], missing: List[str]):
    total = len(matched) + len(missing)
    if total == 0:
        return 0
    return round((len(matched) / total) * 100)

