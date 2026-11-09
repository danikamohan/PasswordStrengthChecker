# password.py

def main():
    user_password = input('Enter your password: ')
    strength_score = 0
    if len(user_password) < 1:
        print("Please enter a valid password")
        return

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
    if user_password.isalnum() == False:
        strength_score += 1




        
    # then check if it has at least one number
    has_digit = False
    for letter in user_password:
        if letter.isdigit() == True:
            has_digit = True
    if has_digit:
        strength_score += 1


    print(strength_score)

if __name__ == "__main__":
    main()