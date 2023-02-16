import re

# Registration function
def register():
    # Get user input for email/username and password
    username = input("Enter your email/username: ")
    password = input("Enter your password: ")

    # Validate email/username
    if not re.match(r"[^@]+@[^@]+\.[^@]+", username):
        print("Invalid email/username format. Please try again.")
        return

    if "@" in username and "." in username.split("@")[1][:1]:
        print("Invalid email/username format. Please try again.")
        return

    # Validate password
    if not re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{5,16}$", password):
        print("Invalid password format. Please try again.")
        return

    # Save username and password in a file
    with open("database.txt", "a") as f:
        f.write(f"{username},{password}\n")
    print("Registration successful.")

# Login function
def login():
    # Get user input for email/username and password
    username = input("Enter your email/username: ")
    password = input("Enter your password: ")

    # Check if username and password exist in the file
    with open("database.txt", "r") as f:
        for line in f:
            if line.strip() == f"{username},{password}":
                print("Login successful.")
                return
            elif line.split(",")[0] == username:
                # User exists, but incorrect password
                print("Incorrect password. Please try again.")
                forgot_password_choice = input("Forgot your password? (y/n): ")
                if forgot_password_choice.lower() == "y":
                    # Retrieve original password based on username
                    original_password = line.split(",")[1].strip()
                    print(f"Your original password is: {original_password}")
                    return
                else:
                    return
    print("Username not found. Please register.")


# Main program
while True:
    choice = input("Enter 1 to register, 2 to login, or 3 to exit: ")
    if choice == "1":
        register()
    elif choice == "2":
        login()
    elif choice == "3":
        break
    else:
        print("Invalid choice. Please try again.")
