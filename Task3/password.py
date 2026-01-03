import random
import string

def generate_password(length, complexity):
    if complexity == "low":
        characters = string.ascii_lowercase

    elif complexity == "medium":
        characters = string.ascii_lowercase + string.ascii_uppercase + string.digits

    elif complexity == "high":
        characters = (
            string.ascii_lowercase +
            string.ascii_uppercase +
            string.digits +
            string.punctuation
        )
    else:
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def main():
    print("🔐 PASSWORD GENERATOR")

    try:
        length = int(input("Enter password length: "))
        if length <= 0:
            print("❌ Password length must be greater than 0.")
            return

        print("\nChoose password complexity:")
        print("1. Low (letters only)")
        print("2. Medium (letters + numbers)")
        print("3. High (letters + numbers + symbols)")

        choice = input("Enter your choice (1/2/3): ").strip()

        if choice == "1":
            complexity = "low"
        elif choice == "2":
            complexity = "medium"
        elif choice == "3":
            complexity = "high"
        else:
            print("❌ Invalid complexity choice.")
            return

        password = generate_password(length, complexity)
        print("\n✅ Generated Password:")
        print(password)

    except ValueError:
        print("❌ Please enter a valid number.")


if __name__ == "__main__":
    main()
