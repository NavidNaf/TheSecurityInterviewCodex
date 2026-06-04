import time


VALID_USERNAME = "admin"

# Vulnerable point: the password is stored in plaintext.
# A safer design would store a salted password hash and verify the hash instead.
VALID_PASSWORD = "OptiPass123"


def insecure_compare(user_input, real_value):
    # Vulnerable point: this comparison stops as soon as it finds a mismatch. Because each matched character takes a little longer, someone can guess the password one character at a time by measuring response time.
    if len(user_input) != len(real_value):
        return False

    for i in range(len(real_value)):
        if user_input[i] != real_value[i]:
            return False
        time.sleep(0.05)

    return True


def login(username, password):
    # Vulnerable point: username and password are checked directly against stored plaintext values instead of using hashed password verification.
    if username == VALID_USERNAME and insecure_compare(password, VALID_PASSWORD):
        return "Login successful"

    return "Invalid username or password"


if __name__ == "__main__":
    username = input("Username: ")
    password = input("Password: ")
    print(login(username, password))
