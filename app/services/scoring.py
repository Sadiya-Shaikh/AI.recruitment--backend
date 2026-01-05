SKILL_WEIGHTS = {
    "python": 2,
    "docker": 2,
    "aws": 3,
    "fastapi": 1,
    "git": 1
}

def weighted_score(matched: list, jd_skills: list) -> int:
    if not jd_skills:
        return 0

    total = sum(SKILL_WEIGHTS.get(s, 1) for s in jd_skills)
    gained = sum(SKILL_WEIGHTS.get(s, 1) for s in matched)

    return int((gained / total) * 100)
