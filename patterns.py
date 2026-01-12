import re

COMMON_PATTERNS = [
    "123", "password", "qwerty", "admin", "letmein"
]

def has_common_patterns(password):
    lower = password.lower()

    if any(p in lower for p in COMMON_PATTERNS):
        return True

    if re.search(r"(.)\1{2,}", password):
        return True

    if re.search(r"(19|20)\d{2}", password):
        return True

    return False
