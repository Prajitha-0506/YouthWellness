import streamlit as st
import pandas as pd
import plotly.express as px
import datetime
import os

st.set_page_config(page_title="Youth Mood Tracker", page_icon="😃")

MOOD_FILE = "mood_log.csv"
moods = {
    "😀 Happy": "Happy", 
    "😢 Sad": "Sad", 
    "😠 Angry": "Angry", 
    "😐 Neutral": "Neutral", 
    "😫 Stressed": "Stressed",
    "🤩 Excited": "Excited"
}

def load_mood_data():
    if not os.path.exists(MOOD_FILE):
        return pd.DataFrame(columns=["Date", "Mood", "Journal"])
    return pd.read_csv(MOOD_FILE)

def save_mood_data(entry):
    df = load_mood_data()
    df = pd.concat([df, pd.DataFrame([entry])], ignore_index=True)
    df.to_csv(MOOD_FILE, index=False)

# Main App
st.title("Youth Mental Wellness Mood Tracker")
st.markdown("#### Log your daily mood and thoughts, visualize your mental wellness journey!")

today = datetime.date.today()
selected_mood = st.radio("Select today's mood:", list(moods.keys()))
journal = st.text_area("Write today's journal (optional)", "")

if st.button("Log Today's Mood 🎉"):
    entry = {"Date": str(today), "Mood": moods[selected_mood], "Journal": journal}
    save_mood_data(entry)
    st.success("Mood and journal logged. Keep going strong!")

# Load and Display Entries
df = load_mood_data()
if not df.empty:
    st.subheader("📜 Your Mood Journals")
    st.dataframe(df.sort_values(by="Date", ascending=False), use_container_width=True)

    # Line Chart: Mood Over Time
    st.subheader("📈 Mood Trends Over Time")
    df['Mood_Num'] = df['Mood'].map({"Happy":5, "Excited":4, "Neutral":3, "Stressed":2, "Sad":1, "Angry":0})
    fig = px.line(df, x="Date", y="Mood_Num", markers=True, title="Mood over Time")
    fig.update_traces(line_color="#00BFFF")
    fig.update_layout(yaxis=dict(tickvals=[0,1,2,3,4,5], ticktext=["Angry","Sad","Stressed","Neutral","Excited","Happy"]))
    st.plotly_chart(fig, use_container_width=True)

    # Frequency Chart
    st.subheader("📊 Mood Frequency")
    freq_fig = px.histogram(df, x="Mood", color="Mood", title="How Often Each Mood Occurs", 
                            category_orders={"Mood":["Angry","Sad","Stressed","Neutral","Excited","Happy"]})
    st.plotly_chart(freq_fig, use_container_width=True)

    # Download CSV
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("Download Your Mood Log as CSV", csv, "mood_log.csv", "text/csv")

else:
    st.info("No mood entries yet. Add your first mood now!")

# Credits
st.markdown("---\n*Made for GenAI Exchange Hackathon: Mood Tracker by Siri/Lakshmi*")
