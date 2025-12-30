from typing import List, Set

from app.utils.skill_dictionary import SKILL_ALIASES

def match_skills(resume_skills, jd_text):
    jd_text = jd_text.lower()
    matched = []
    missing = []

    for skill, aliases in SKILL_ALIASES.items():
        found_in_jd = any(alias in jd_text for alias in aliases)
        found_in_resume = skill.lower() in [s.lower() for s in resume_skills]

        if found_in_jd and found_in_resume:
            matched.append(skill)
        elif found_in_jd and not found_in_resume:
            missing.append(skill)

    return matched, missing

KNOWN_SKILLS = {
    "python", "java", "javascript", "react", "node",
    "express", "mongodb", "sql", "git", "github",
    "docker", "aws", "fastapi", "flask",
    "html", "css", "linux"
}


def calculate_score(matched, jd_skills):
    if not jd_skills:
        return 0
    return int((len(matched) / len(jd_skills)) * 100)

