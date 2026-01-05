from app.utils.skill_dictionary import SKILL_ALIASES
from app.services.scoring import weighted_score

def calculate_score(matched: list, jd_skills: list) -> int:
    if not jd_skills:
        return 0
    return int((len(matched) / len(jd_skills)) * 100)


def analyze_jd_vs_resume(resume_skills: list, jd_text: str):
    jd_text = jd_text.lower()

    jd_skills = []
    matched = []
    missing = []

    resume_lower = {s.lower() for s in resume_skills}

    for skill, aliases in SKILL_ALIASES.items():
        if any(alias in jd_text for alias in aliases):
            jd_skills.append(skill)
            if skill in resume_lower:
                matched.append(skill)
            else:
                missing.append(skill)

    score = weighted_score(matched, jd_skills)

    return {
        "match_score": score,
        "matched_skills": matched,
        "missing_skills": missing,
        "jd_skills": jd_skills
    }
