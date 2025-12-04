from .patterns import DANGEROUS_PATTERNS
import re

def suggest_fix(prompt: str) -> str:
    """
    Suggests a fixed version of the prompt by removing dangerous patterns.

    Args:
        prompt (str): The input prompt to be fixed.
    """
    safe_prompt = re.sub(r"[^a-zA-Z0-9\s]", "", prompt)
    for pattern in DANGEROUS_PATTERNS:
        safe_prompt = re.sub(pattern, "[REMOVED]", safe_prompt, flags=re.IGNORECASE)
    safe_prompt = re.sub(r"\s+", " ", safe_prompt).strip()
    return safe_prompt