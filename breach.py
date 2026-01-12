import hashlib
import requests

def check_breach(password):
    sha1 = hashlib.sha1(password.encode()).hexdigest().upper()
    prefix = sha1[:5]
    suffix = sha1[5:]

    url = f"https://api.pwnedpasswords.com/range/{prefix}"

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
    except requests.RequestException:
        # Fail safely: assume not breached if API is unreachable
        return False

    hashes = (line.split(":")[0] for line in response.text.splitlines())
    return suffix in hashes
