COMMON_SKILLS = [
    "python", "java", "sql", "excel", "react", "node",
    "fastapi", "django", "aws", "git", "docker"
]

def extract_skills(text: str) -> list[str]:
    text_lower = text.lower()
    found = []

    for skill in COMMON_SKILLS:
        if skill in text_lower:
            found.append(skill.capitalize())

    return list(set(found))
