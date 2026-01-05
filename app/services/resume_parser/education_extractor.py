import re

def extract_education(text: str) -> str:
    match = re.search(
        r"(bachelor|b\.sc|bcs|master|m\.sc)",
        text.lower()
    )
    return match.group(0).upper() if match else "Not found"
