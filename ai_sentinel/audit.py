import re

DANGEROUS_PATTERNS = [
    r"ignore previous instructions",
    r"malicious",
    r"jailbreak",
    r"system override",
]

def detect_prompt_injection(prompt: str) -> bool:
    """
    Detects if the given prompt contains any known prompt injection patterns.

    Args:
        prompt (str): The input prompt to be analyzed.
    """
    flags = []
    for pattern in DANGEROUS_PATTERNS:
        if re.search(pattern, prompt, re.IGNORECASE):
            flags.append(pattern)
    return flags

def audit(prompt: str) -> dict:
    return {
        "injection_patterns": detect_prompt_injection(prompt),
        "length" : len(prompt),
        "has_code": bool(re.search(r"\b(def |import |class )", prompt)),
    }