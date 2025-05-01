import os
from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from telethon.errors import BotTokenInvalidError

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def main():
    clear_screen()
    print("=== Telegram Bot String Session Generator (GramJS) ===\n")

    try:
        api_id = int(input("Enter your API ID: "))
        api_hash = input("Enter your API Hash: ").strip()
        bot_token = input("Enter your Bot Token: ").strip()

        print("\nGenerating session...")

        with TelegramClient(StringSession(), api_id, api_hash) as client:
            client.start(bot_token=bot_token)
            string_session = client.session.save()

        print("\n=== Your String Session ===")
        print(string_session)
        print("\nKeep this string safe and do not share it.")

    except BotTokenInvalidError:
        print("\nERROR: The bot token you provided is invalid. Please check it and try again.")
    except ValueError:
        print("\nERROR: Invalid API ID. It must be a number.")
    except Exception as e:
        print(f"\nUnexpected error occurred: {e}")

if __name__ == "__main__":
    main()
