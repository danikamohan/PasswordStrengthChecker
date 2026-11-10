# password.py

def check_password(password):
    strength_score = 0

    # check if input is greater or equal to 12
    is_long_enough = False
    if len(password) >= 12:
        strength_score += 1
        is_long_enough = True

    # then check if it has a capital letter
    has_capital = False
    for letter in password:
        if letter.isupper():
            has_capital = True
    if has_capital:
        strength_score += 1

    # then check if it has a special char
    has_special_char = False
    if not password.isalnum():
        strength_score += 1
        has_special_char = True

    # then check if it has at least one number
    has_digit = False
    for letter in password:
        if letter.isdigit():
            has_digit = True
    if has_digit:
        strength_score += 1

    return strength_score, is_long_enough, has_capital, has_special_char, has_digit


def main():
    user_password = input('Enter your password: ')
    if len(user_password) < 1:
        print("Please enter a valid password")
        return

    strength_score, is_long_enough, has_capital, has_special_char, has_digit = check_password(user_password)

    # convert strength score to words
    if strength_score == 4:
        print("Strength: Strong")
    elif strength_score == 3:
        print("Strength: Good")
    elif strength_score == 2:
        print("Strength: Fair")
    else:
        print("Strength: Weak")

    # print out what password is missing
    print("Your password should have:")
    if is_long_enough:
        print("(✓) At least 12 characters")
    else:
        print("(x) At least 12 characters")
    if has_capital:
        print("(✓) One uppercase letter")
    else:
        print("(x) One uppercase letter")
    if has_special_char:
        print("(✓) One symbol or special character")
    else:
        print("(x) One symbol or special character")
    if has_digit:
        print("(✓) One number")
    else:
        print("(x) One number")


if __name__ == "__main__":
    main()