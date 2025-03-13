
import streamlit as st
import re
import random
import string

st.set_page_config(page_title="Login", page_icon="🔐", layout="centered")

st.title("🔐 Login")

# Background & Password Container CSS
st.markdown(
    """
    <style>
        .stApp {
            background-image: url('https://images.unsplash.com/photo-1432821596592-e2c18b78144f?fm=jpg&q=60&w=3000&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NHx8bG9naW58ZW58MHx8MHx8fDA%3D');
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }
        .password-container {
            background: rgba(255, 255, 255, 0.95);
            padding: 10px 15px;
            border-radius: 8px;
            font-size: 14px;
            color: black;
            width: 260px;
            box-shadow: 0px 2px 6px rgba(0,0,0,0.3);
            margin-top: -8px;
            position: relative;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Function to generate a strong password
def generate_password():
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    return "".join(random.choice(chars) for _ in range(12))

# Function to check password strength
def check_password_strength(password):
    score = 0
    suggestions = []
    blacklist = ["password", "123456", "password123", "qwerty", "admin123"]

    # Blacklist check
    if password.lower() in blacklist:
        return "❌ Weak Password", ["⚠️ Do not use common passwords like 'password123' or 'admin123'."]

    # Length check
    if len(password) >= 12:
        score += 2  # More weight for longer passwords
    elif len(password) >= 8:
        score += 1
    else:
        suggestions.append("🔴 Use at least 8 characters.")

    # Upper & lower case check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("🟠 Add uppercase & lowercase letters.")

    # Numbers check
    if re.search(r"\d", password):
        score += 1
    else:
        suggestions.append("🟡 Add a number (0-9).")

    # Special character check
    if re.search(r"[!@#$%^&*]", password):
        score += 2  # More weight for special characters
    else:
        suggestions.append("🟢 Add a special character (!@#$%^&*).")

    # Scoring levels
    if score >= 5:
        return "✅ Strong Password", []
    elif score >= 3:
        return "⚠️ Moderate Password", suggestions
    else:
        return "❌ Weak Password", suggestions

# Input fields
email = st.text_input("Enter Email")
password = st.text_input("Enter Password", type="password")

# Password Generator Button
if st.button("Generate Strong Password"):
    st.text(f"Suggested Password: {generate_password()}")

# Live password validation (Container Close to Input)
if password:
    strength, suggestions = check_password_strength(password)
    st.markdown(f"<div class='password-container'><b>{strength}</b><br>", unsafe_allow_html=True)
    for suggestion in suggestions:
        st.markdown(f"✅ {suggestion}", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# Login button
if st.button("Login"):
    if password and strength == "✅ Strong Password":
        st.success("✅ Login Successful!")
    else:
        st.error("❌ Please enter a strong password before logging in.")
