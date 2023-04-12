#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
      API_ID:9585138
      API_HASH:"85471aa423d87a98f164b7b24d502c17"
      BOT_TOKEN:"6186823131:AAH3EtKysnEVR40-tz_EkPwVYMxuhLxRd08"
      SESSION:"AQC22QnWJZvREYamSG6GodKyQXg3__VLuezNayx3Xpq82KVcO3xmL28wwG7yIlekaJbyJdPBqIPOazqW5zsa7aXHBMFJHE8EY2JMDN9hhY457pamLS3o6xmUYtOKtZ7C3QUWQ5zTT7qA67nJCpYXKD2-THVukroF59P1dmWzV4N0RLC5hfYxRMkQoUX6d7ycdssPfTdQPj_YLh7zAv5jnN-F4d27HMYFum7zI6b4u7On0cKmTFHetbC7FHNXigyadN9PX185qdwgFw14EF37eIobm46aakjL-0mK6rspJo-Z6PXU_KHpfkn6zLxxyUeM9o0Z_E1D562iTy3VWsT3rLSxAAAAAVS4XqcA"
      AUTH:5716336295
      FORCESUB:"asalidrbot"


bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client(
    session_name=SESSION, 
    api_hash=API_HASH, 
    api_id=API_ID)

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
