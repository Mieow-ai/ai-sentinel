from .patterns import DANGEROUS_PATTERNS
import re

def detect_prompt_injection(prompt: str) -> list:
    """
    Detects dangerous patterns in a prompt.
    Returns a list of matched patterns.
    """
    safe_prompt = re.sub(r"[^a-zA-Z0-9\s]", " ", prompt)
    safe_prompt = re.sub(r"\s+", " ", safe_prompt).strip()

    flags = []
    for pattern in DANGEROUS_PATTERNS:
        if re.search(pattern, safe_prompt, re.IGNORECASE | re.DOTALL):
            flags.append(pattern)
    return flags