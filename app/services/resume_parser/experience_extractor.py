import re

def extract_experience(text: str) -> int:
    patterns = [
        r"(\d+)\+?\s+years?",
        r"over\s+(\d+)\s+years",
        r"experience\s+of\s+(\d+)\s+years"
    ]

    text = text.lower()
    for pattern in patterns:
        match = re.search(pattern, text)
        if match:
            return int(match.group(1))

    return 0
