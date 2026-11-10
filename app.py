# app.py

import streamlit as st
from password import check_password


def show_rule(passed, rule_text):
    if passed:
        st.write("✓ " + rule_text)
    else:
        st.write("✗ " + rule_text)


st.title("Password Strength Checker")

# save empty spot for the results, so the password box can go below it
results = st.container()

user_password = st.text_input("Enter your password", type="password")

if user_password:
    strength_score, is_long_enough, has_capital, has_special_char, has_digit = check_password(user_password)

    with results:
        if strength_score == 4:
            st.success("Strength: Strong. Great password!")
        elif strength_score == 3:
            st.write("### :green[Strength: Good]")
        elif strength_score == 2:
            st.write("### :orange[Strength: Fair]")
        else:
            st.write("### :red[Strength: Weak]")

        st.write("Your password should have:")
        show_rule(is_long_enough, "At least 12 characters")
        show_rule(has_capital, "One uppercase letter")
        show_rule(has_special_char, "One symbol or special character")
        show_rule(has_digit, "One number")