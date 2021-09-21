from os import getenv

from dotenv import load_dotenv

load_dotenv()
que = {}
SESSION_NAME = getenv("SESSION_NAME", "BQAYwzDtoLVfzz5WtOAVKk5AiABXuQDDZA53hOuksWFYavq0_FDnasgIWRQeinbC_3CSSsQstikpYDFLvBo9zDA1UmdNK_b8RFiFzD1Wt2Nh-IE2qS55fWORchdHW4KzqIos50QyFjOx-qTAmE3tkfeedNAU7LQQBx-BXLSZDq6fcq9SpNh3Cl5cDe3Lk6C_0RK0lMWj0dL8C31S3xdUlk4P7BdP9GsdVB-BdaTnViO6UWXFVFpMnsghIE1LnXAvNuf57lLWV1eJ_HDoBxv6Xkt3I8BghGY0gRbUTM7fhAGTN2jnZCRH-05MrW0GD6Cwys38IpfZG8bhhgPbaZPeitWiVwG0CQA")
BOT_TOKEN = getenv("BOT_TOKEN", "1937087520:AAGPzDeqUUEgNDTpDoUL3Gv8aPtUkXLOZV8")
BOT_NAME = getenv("BOT_NAME", "𝐩𝐚𝐭𝐫𝐢𝐜𝐢𝐚𝐗𝐦𝐮𝐬𝐢𝐜")
admins = {}
API_ID = int(getenv("API_ID", "7858704"))
API_HASH = getenv("API_HASH", "374b22267a25bea0de48150075a22c1d")

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "2012882227").split()))
