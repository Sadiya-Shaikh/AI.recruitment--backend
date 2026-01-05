SKILL_ALIASES = {
    "python": ["python", "python3", "py"],
    "docker": ["docker", "docker-compose"],
    "aws": ["aws", "amazon web services"],
    "fastapi": ["fastapi", "fast api"],
    "git": ["git", "github", "gitlab"],
}

def normalize_skills(raw_text: str) -> list[str]:
    text = raw_text.lower()
    found = set()

    for skill, aliases in SKILL_ALIASES.items():
        for alias in aliases:
            if alias in text:
                found.add(skill)

    return sorted(found)
