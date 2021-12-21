import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "Neko")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
OWNER_NAME = getenv("OWNER_NAME", "Lovely Boy")
ALIVE_NAME = getenv("ALIVE_NAME", "Levina")
BOT_USERNAME = getenv("BOT_USERNAME", "NekoXRobot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Neko Assistant")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "NekoXSupport")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "levinachannel")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/432fa6ac692054f5a3527.png")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/Hodacka/Music")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/006bb8da78cab05216112.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/52f1de7ddf951a0fa3571.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/5a70b2fcaa47870ef2e6d.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/cf776e22bd048b2fa222b.png")
