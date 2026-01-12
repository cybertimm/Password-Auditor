from getpass import getpass

from strength import calculate_entropy
from patterns import has_common_patterns
from reuse import detect_reuse
from breach import check_breach

def main():
    print("Password Security Analyzer\n")

    pw1 = getpass("Enter password: ")
    pw2 = getpass("Re-enter password (reuse check): ")

    passwords = [pw1, pw2]

    entropy = calculate_entropy(pw1)
    patterns = has_common_patterns(pw1)
    reused = detect_reuse(passwords)
    breached = check_breach(pw1)

    print("\nResults:")
    print("-" * 30)

    print(f"Entropy: {entropy} bits")

    if entropy < 40:
        print("❌ Weak entropy")
    elif entropy < 60:
        print("⚠️ Moderate entropy")
    else:
        print("✅ Strong entropy")

    if patterns:
        print("❌ Common or predictable pattern detected")

    if reused:
        print("❌ Password reuse detected")

    if breached:
        print("⚠️ Found in known data breaches")
    else:
        print("✅ Not found in breach databases")

if __name__ == "__main__":
    main()
