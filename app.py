# app.py

import streamlit as st
from password import check_password  # reuse checks


# show check or x
def show_rule(passed, rule_text):
    if passed:
        st.write("✓ " + rule_text)
    else:
        st.write("✗ " + rule_text)


# draw 4 boxes from wireframe
def show_strength_bar(score):
    colors = ["#C0423F", "#E07142", "#EBCB6F", "#93E27A"]  # red, orange, yellow, green
    filled = max(score, 1)  # min 1 box

    boxes = ""
    for i in range(4):  # i = 0 to 3
        if i < filled:
            color = colors[i]  # filled color
        else:
            color = "#D9D9D9"  # empty gray
        # {color} goes into html, 1 div = 1 box
        boxes += f'<div style="flex: 1; height: 28px; background-color: {color}; border: 1px solid #333;"></div>'

    # flex = side by side, allow html
    st.markdown(f'<div style="display: flex;">{boxes}</div>', unsafe_allow_html=True)


st.title("Password Strength Checker")

# save spot above input
results = st.container()

# hide typing
user_password = st.text_input("Enter your password", type="password")

# only run if typed
if user_password:
    # unpack results (order matters)
    strength_score, is_long_enough, has_capital, has_special_char, has_digit = check_password(user_password)

    # fill saved spot
    with results:
        show_strength_bar(strength_score)

        # score to words (green for good, yellow hard to read)
        if strength_score == 4:
            st.success("Strength: Strong. Great password!")
        elif strength_score == 3:
            st.write("### :green[Strength: Good]")
        elif strength_score == 2:
            st.write("### :orange[Strength: Fair]")
        else:
            st.write("### :red[Strength: Weak]")

        # rule checklist
        st.write("Your password should have:")
        show_rule(is_long_enough, "At least 12 characters")
        show_rule(has_capital, "One uppercase letter")
        show_rule(has_special_char, "One symbol or special character")
        show_rule(has_digit, "One number")