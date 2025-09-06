import streamlit as st

# App title
st.set_page_config(page_title="Youth Mental Wellness App", layout="wide")
st.title("🌱 Youth Mental Wellness Web App")

# Sidebar navigation
page = st.sidebar.radio("Navigate", ["Home", "Chatbot", "Mood Tracker", "Dashboard"])

# Page routing
if page == "Home":
    st.subheader("Welcome 👋")
    st.write("This is our Generative AI Youth Mental Wellness project. Use the sidebar to explore.")

elif page == "Chatbot":
    st.subheader("💬 Chatbot")
    st.write("Chatbot UI will be added here.")

elif page == "Mood Tracker":
    st.subheader("📊 Mood Tracker")
    st.write("Mood entry form will be added here.")

elif page == "Dashboard":
    st.subheader("📈 Dashboard")
    st.write("Visualizations will appear here.")