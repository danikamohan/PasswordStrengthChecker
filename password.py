# password.py

def main():
    user_password = input('Enter your password: ')
    strength_score = 0

    # check if input is greater or equal to 12
    if len(user_password) >= 12:
        strength_score += 1
    
    # then check if it has a capital letter
    has_capital = False
    for letter in user_password:
        if letter.isupper() == True:
            has_capital = True
    if has_capital:
        strength_score += 1

    # then check if it has a special char
    # then check if it has at least one number

    print(strength_score)

if __name__ == "__main__":
    main()