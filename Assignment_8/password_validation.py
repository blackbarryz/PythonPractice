def check_password(password):
    """Checks if a password meets all policy requirements."""
    # Check length
    if len(password) < 8:
        return False, "Password must be at least 8 characters long."
    
    # Check for invalid characters (spaces or symbols)
    if not password.isalnum():
        return False, "Password may only contain letters and digits (no spaces or symbols)."
    
    # Initialize flags for required character types
    has_upper = False
    has_lower = False
    has_digit = False
    
    # Iterate through each character to test rules
    for ch in password:
        if ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch.isdigit():
            has_digit = True

    # Validate that all required types were found
    if not has_upper:
        return False, "Password must contain at least one uppercase letter."
    if not has_lower:
        return False, "Password must contain at least one lowercase letter."
    if not has_digit:
        return False, "Password must contain at least one digit."
        
    return True, "Password is valid!"

def main():
    print("--- Password Validator ---")
    user_password = input("Enter a password to validate: ").strip()
    
    is_valid, message = check_password(user_password)
    print(message)

if __name__ == '__main__':
    main()
