import random
import string

#  list of common passwords
common_pass = ['password', 'admin', '123456', 'qwerty', 'letmein', 'welcome', 'monkey', 'password1']

def generate_password(length=8):
    """Generate a random password."""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def is_acceptable(password):
    """Check if the password meets acceptance criteria."""
    # Check for special symbols
    has_special = any(char in string.punctuation for char in password)
    
    # Check if the password is in the common_pass list
    not_in_common_pass = password not in common_pass
    
    return has_special and not_in_common_pass

iterations = 40

accepted_passwords = []

for i in range(iterations):
    password = generate_password()
    if is_acceptable(password):
        accepted_passwords.append(password)
    else:
        # Unaccepted passwords get deleted 
        pass

print("Accepted Passwords:")
for password in accepted_passwords:
    print(password)
