import re

def check_password(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add an uppercase letter.")
    
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add a lowercase letter.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Add a number.")

    if re.search(r"[^A-Za-z0-9]", password):
        score += 1
    else:
        feedback.append("Add a special character.")

    return score, feedback

def main():
    password = input("Enter a password to check: ")
    score, feedback = check_password(password)

    print(f"\nStrength score: {score}/5")

    if score == 5:
        print("Strong password!")
    elif score >= 3:
        print("Decent password, but it can be better.")
    else:
        print("Weak password.")

    if feedback:
        print("\nTIps:")
        for item in feedback:
            print(f" - {item}")

if __name__ =="__main__":
    main()

