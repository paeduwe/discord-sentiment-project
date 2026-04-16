import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)

st.title("Discord Sentiment Dashboard")

# load data
df = pd.read_sql("SELECT * FROM messages", engine)

if df.empty:
    st.write("No data yet")
else:
    # convert timestamp
    df["timestamp"] = pd.to_datetime(df["timestamp"])

    # --- Time Series ---
    st.subheader("Messages Over Time")

    time_series = df.set_index("timestamp").resample("1h").size()

    st.line_chart(time_series)

    # --- Sentiment Pie ---
    st.subheader("Sentiment Distribution")

    positive = df[df["sentiment_score"] > 0].shape[0]
    negative = df[df["sentiment_score"] < 0].shape[0]

    pie_data = pd.DataFrame({
        "Sentiment": ["Positive", "Negative"],
        "Count": [positive, negative]
    })

    st.bar_chart(pie_data.set_index("Sentiment"))


    # toxicity
    df["is_toxic"] = df["sentiment_score"] < 0
    toxicity = df.set_index("timestamp").resample("1h")["is_toxic"].mean()

    st.subheader("Toxicity Over Time")
    st.line_chart(toxicity)

    # --- Stats ---
    st.subheader("Statistics")

    st.write("Total messages:", len(df))
    st.write("Positive:", positive)
    st.write("Negative:", negative)