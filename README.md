
# Password Strength Checker
![Python](https://img.shields.io/badge/Python-3.13-ff69b4)
![Figma](https://img.shields.io/badge/Designed_in-Figma-a259ff)

This is a Python program that not only checks the strength of a password but also lets you know what else you need to make it stronger!

## Why I Built This

I built this to jump back into Python and explore coding keeping the user in mind, which is why I started by sketching in Figma.

## Features

- Checks 4 rules: 12+ characters, an uppercase letter, a special character, and a number
- Rates your password as Weak, Fair, Good, or Strong
- Shows a checklist so you know exactly what to fix

## Demo
![Demo](demo.gif)

```
Enter your password: Glinda
Strength: Weak
Your password should have:
(x) At least 12 characters
(✓) One uppercase letter
(x) One symbol or special character
(x) One number
```

## Design Process

I really wanted to first try and sketch what a user might see using this application. I tried to keep the colors of the strengths very familiar and keep text at a minimum to avoid confusion. 

![Wireframe](wireframe.png)

Choices I made:

- Password box at the bottom: I placed the text box near the bottom of the screen so it’s easy to reach with your thumb and sits right above the keyboard.
- Red to green strength bar: It was a familiar set up compared to traffic lights. 
- ✓ and x checklist: This was to show user what they can do to make their password stronger.

## Design Decisions

- Spaces count as special characters: Many websites and security guidelines count spaces as special characters, since long passphrases with spaces can be very strong
- Empty passwords: I made it so if a user does not enter a password, an error message gets sent out that tells them to enter a valid one! 

## How to Run

Make sure Python 3 is installed, then run:

```
python3 password.py
```

## What I Learned

- Using loops to check each character in a string
- Using True/False variables to keep track of what I found
- Using if / elif / else to choose between options
- Input validation (checking input before using it)
- Designing in Figma before coding (this helped shape my code a lot!)
- Using Git and GitHub to save my progress

## What's Next

- A web version using Streamlit with a colored strength bar that matches my wireframe

---

Built by Danika Mohan 
· [GitHub](https://github.com/danikamohan) 
· [LinkedIn](https://linkedin.com/in/danimohan)