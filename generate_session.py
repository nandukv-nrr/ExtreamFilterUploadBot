from pyrogram import Client
import asyncio
import os

# Create a temporary client to generate the string
async def generate_string():
    print("This script will generate a Pyrogram Session String for your Bot.")
    print("You will need your API_ID, API_HASH, and BOT_TOKEN.")
    
    api_id = input("Enter API_ID: ")
    api_hash = input("Enter API_HASH: ")
    bot_token = input("Enter BOT_TOKEN: ")
    
    async with Client("temp_session", api_id=api_id, api_hash=api_hash, bot_token=bot_token, in_memory=True) as app:
        print("\nSending a message to Saved Messages...")
        try:
            await app.send_message("me", "Session String Generated Successfully!")
        except Exception as e:
            print(f"Could not send message: {e}")
            
        session_string = await app.export_session_string()
        print("\n\nHERE IS YOUR SESSION STRING (Copy everything below):")
        print(f"\n{session_string}\n")
        print("Done! thoroughfully copy the string above and set it as your SESSION environment variable in Koyeb.")

if __name__ == "__main__":
    asyncio.run(generate_string())
