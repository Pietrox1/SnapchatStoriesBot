import logging
import os

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
LOGGER = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)


class ENV_VARS(object):
    API_ID = int(os.environ.get("API_ID" , "16156788"))
    API_HASH = os.environ.get("API_HASH" , "8153259ab0f78c9d6e5103e6a927d68b")
    BOT_TOKEN = os.environ.get("BOT_TOKEN" , "6506281957:AAEAFVjvgFNiwivIGHBLgZSwYkR9O3oqOuc")
    BOT_USERNAME = os.environ.get("BOT_USERNAME" , "pietro_2023_bot")
    #AUTH_USER = int(os.environ.get("AUTH_USER", 5071059420))


Config = ENV_VARS

handler = Config.BOT_USERNAME


class CMD(object):
    START = ["start", f"start@{handler}"]
