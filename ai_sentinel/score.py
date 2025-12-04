from .detection import detect_prompt_injection


def score(prompt : str) -> float:
    """
    Scores the prompt based on the presence of dangerous patterns.

    Args:
        prompt (str): The input prompt to be scored.
    """
    score = 0.0
    if detect_prompt_injection(prompt):
        score += 0.7
    if len(prompt) > 200 :
        score += 0.1
        
    words = prompt.lower().split()
    unique_words = set(words)
    repetition_ratio = 1 - len(unique_words) / len(words) if words else 0
    if repetition_ratio > 0.3:
        score += 0.2
    return min(score, 1.0)