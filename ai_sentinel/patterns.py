import json
import os

def load_patterns() -> list:
    file_path = os.path.join(os.path.dirname(__file__), 'dangerous_patterns.json')
    data = {}
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    patterns = []
    for category, plist in data.items():
        patterns.extend(plist)
        
    return patterns 

DANGEROUS_PATTERNS = load_patterns()