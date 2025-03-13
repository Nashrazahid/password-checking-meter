# import streamlit as st 
# import re

# st.set_page_config(page_title="login",page_icon="🔐",layout="centered")

# st.title("🔐Login")


# st.markdown("""
#     <style>
#         .stApp{
#            background-image: url('https://images.unsplash.com/photo-1432821596592-e2c18b78144f?fm=jpg&q=60&w=3000&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NHx8bG9naW58ZW58MHx8MHx8fDA%3D');
#             background-size: cover;
#             background-position: center;
#             background-repeat: no-repeat;
#         }
#     </style>
#             """,
#     unsafe_allow_html=True,)


# def check_password_strength(password):
#     score = 0

#     if len(password)  >= 8:
#         score += 1
#     else:
#         print("password should be atleast 8 characters long")

    
#     if re.search(r"[A-Z]",password) and re.search(r"[a-z],password"):
#         score += 1
#     else:
#         print("include both uppercase and lower case letters.")


#     if re.search(r"\d",password):
#         score += 1
#     else:
#         print("add atleast one number (0-9).")    

#     if re.search(r"[!@#$%^&*]",password):
#         score += 1
#     else:
#         print("add at least one special character(!@#$%^&*)")

#     if score == 4:
#         print("strong password")
#     elif score == 3:
#         print("moderate password , Consider adding more security features")
#     else:
#         print("weak password improve it using the suggestion above")


# st.text_input("enter email")
# password = st.text_input("enter password",type="password")
# st.button("login")
# check_password_strength(password)








import streamlit as st
import re

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
            padding: 5px 10px;
            border-radius: 6px;
            font-size: 12px;
            color: black;
            width: 220px;
            box-shadow: 0px 2px 4px rgba(0,0,0,0.2);
            margin-top: -8px; /* Password field ke bilkul kareeb */
            position: relative;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Function to check password strength
def check_password_strength(password):
    score = 0
    suggestions = []

    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("🔴 Use at least 8 characters.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("🟠 Add uppercase & lowercase letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        suggestions.append("🟡 Add a number (0-9).")

    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        suggestions.append("🟢 Add a special character (!@#$%^&*).")

    if score == 4:
        return "✅ Strong Password", []
    elif score == 3:
        return "⚠️ Moderate Password", suggestions
    else:
        return "❌ Weak Password", suggestions

# Input fields
email = st.text_input("Enter Email")
password = st.text_input("Enter Password", type="password")

# Live password validation (Container Close to Input)
if password:
    strength, suggestions = check_password_strength(password)
    if strength != "✅ Strong Password":
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
