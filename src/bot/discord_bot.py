import discord
import os
from dotenv import load_dotenv
from src.db.models import SessionLocal, Message

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')


#auto to if mesa einai gia an to mesasge einai tou idiou 
# tou bot na mhn grafetai sto terminal
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    username = str(message.author)
    text = message.content

    print(f"{username}: {text}")


    #save message
    session = SessionLocal()

    msg = Message(
        username=username,
        text=text
    )
    try:
        session.add(msg)
        session.commit()
    except Exception as e:
        session.rollback()   # IMPORTANT in production
        print("DB error:", e)
    finally:
        session.close()
        
        

client.run(TOKEN)


