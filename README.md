# Discord Sentiment Analysis Pipeline

A real-time data pipeline that collects Discord messages, stores them in PostgreSQL, performs sentiment analysis using a pretrained NLP model, and visualizes results through an interactive dashboard.

---

# Prjoject Overview

This system demonstrates a full end-to-end data pipeline:

1. **Data Ingestion** – Discord bot listens to messages in real time
2. **Data Storage** – Messages are stored in a PostgreSQL database
3. **AI Processing** – Sentiment analysis is applied using a pretrained NLP model
4. **Automation** – Background scheduler processes new messages every 10 minutes
5. **Visualization** – Interactive dashboard built with Streamlit

---

# Tech Stack

- Python
- Discord API (discord.py)
- PostgreSQL
- SQLAlchemy (ORM)
- Hugging Face Transformers (sentiment analysis model)
- Streamlit (dashboard)
- Pandas
- Schedule (automation)

---

# Project Structure

src/
│
├── bot/ # Discord bot (data ingestion)
├── db/ # Database models and connection
├── ai/ # Sentiment analysis worker + scheduler
├── dashboard/ # Streamlit dashboard




##  Setup Instructions

### 1. Clone repository

git clone https://github.com/your-username/discord-sentiment-project.git
cd discord-sentiment-project


### 2. Create virtual environment

python -m venv venv
venv\Scripts\activate   # Windows

### 3. Install dependencies

pip install -r requirements.txt


### 4. Create .env file

DISCORD_TOKEN=your_token_here
DATABASE_URL=your_postgres_url_here


### 5. Run components

Start Discord bot:
python -m src.bot.discord_bot

Start AI worker (optional manual run):
python -m src.ai.sentiment_worker

Start scheduler (automated AI processing):
python -m src.ai.run_worker

Launch dashboard:
streamlit run src.dashboard.app