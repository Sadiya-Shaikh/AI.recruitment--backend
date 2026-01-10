from app.services.scoring import semantic_score, weighted_skill_score


CRITICAL_SKILLS = ["linux", "docker", "ci/cd"]


def extract_skills_from_jd(jd: str) -> list[str]:
    keywords = [
        "python", "fastapi", "flask",
        "docker", "aws", "azure", "gcp",
        "git", "linux", "ci/cd"
    ]
    jd_lower = jd.lower()
    return [k for k in keywords if k in jd_lower]


def has_missing_critical(resume_skills: list[str]) -> bool:
    return any(skill not in resume_skills for skill in CRITICAL_SKILLS)


def verdict_engine(final_score: int, missing_critical: bool) -> str:
    if missing_critical:
        return "Rejected"
    elif final_score >= 75:
        return "Recommended"
    elif final_score >= 50:
        return "Consider"
    else:
        return "Rejected"


def analyze_jd_vs_resume(
    resume_skills: list[str],
    resume_text: str,
    jd_text: str
):
    resume_skills = [s.lower() for s in resume_skills]
    jd_skills = extract_skills_from_jd(jd_text)

    matched = list(set(resume_skills) & set(jd_skills))
    missing = list(set(jd_skills) - set(resume_skills))

    skill_score = weighted_skill_score(matched, jd_skills)
    semantic = semantic_score(resume_text, jd_text)

    final = round((0.6 * semantic) + (0.4 * skill_score))

    missing_critical = has_missing_critical(resume_skills)
    verdict = verdict_engine(final, missing_critical)
    

    return {
        "semantic_score": semantic,
        "skill_match_score": skill_score,
        "final_score": final,
        "verdict": verdict,
        "matched_skills": matched,
        "missing_skills": missing,
        "jd_skills": jd_skills
    }


