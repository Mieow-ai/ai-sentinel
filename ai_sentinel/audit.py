import re
from .patterns import DANGEROUS_PATTERNS
from .score import score
from .detection import detect_prompt_injection
from .suggestion import suggest_fix

def audit(prompt: str) -> dict:
    return {
        "input" : prompt,
        "injection_patterns": detect_prompt_injection(prompt),
        "length" : len(prompt),
        "has_code": bool(re.search(r"\b(def |import |class )", prompt)),
        "score" : score(prompt),
        "suggestion" : suggest_fix(prompt)
    }
    
