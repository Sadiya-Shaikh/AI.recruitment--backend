def normalize(skills: list[str]) -> set[str]:
    return {s.lower().strip() for s in skills}


def extract_skills_from_jd(jd: str) -> set[str]:
    keywords = [
        "python", "fastapi", "flask",
        "docker", "aws", "azure", "gcp",
        "git", "linux", "ci/cd"
    ]
    jd_lower = jd.lower()
    return {k for k in keywords if k in jd_lower}


def weighted_score(resume_skills: set[str], jd_skills: set[str]) -> int:
    if not jd_skills:
        return 0

    matched = resume_skills & jd_skills
    return int((len(matched) / len(jd_skills)) * 100)


def analyze_jd_vs_resume(resume_skills: list[str], jd: str) -> dict:
    resume_set = normalize(resume_skills)
    jd_set = extract_skills_from_jd(jd)

    matched = sorted(resume_set & jd_set)
    missing = sorted(jd_set - resume_set)

    score = weighted_score(resume_set, jd_set)

    return {
        "match_score": score,
        "matched_skills": matched,
        "missing_skills": missing,
        "jd_skills": sorted(jd_set)
    }
