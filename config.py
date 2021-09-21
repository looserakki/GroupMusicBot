from os import getenv

que = {}
SESSION_NAME = getenv("SESSION_NAME", "AQBA1jjkQDq8To4HKqQY75xIeHysXbpRTQ8HslLC90u52fF2lWihsxL_ThIaOXYfrm_s6NtGsbuMXtK1wpmUUD9BKsiMW3UzVO9zmLhr3kJsR5_DXmwOMTGwMebRRFzdDaMZ9tjZsP9DIpJ3iCMH-L8haac31ZQjue9qMaQDDQlpbLf1kKkbXmA5NjlZ0j-KxFimKGZnq6RAja-3AjypgQfYFUs4feXvOnJuh_n53vxH5tqMPY6XfKyM6a5dL3WaKCWmSWQi5hwpZBwaWvkn8vNEyQ4SLerLnjpX0dYilDyw0GbsiBWKgV2tZgHutIPrpUT13xOHXtNNN8vs8610siusdN7njwA")
BOT_TOKEN = getenv("BOT_TOKEN", "1937087520:AAGPzDeqUUEgNDTpDoUL3Gv8aPtUkXLOZV8")
BOT_NAME = getenv("BOT_NAME", "𝐩𝐚𝐭𝐫𝐢𝐜𝐢𝐚𝐗𝐦𝐮𝐬𝐢𝐜")
admins = {}
API_ID = int(getenv("API_ID", "8636372"))
API_HASH = getenv("API_HASH", "7dd38153ba6f48bfd990a8067e5b8498")

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "180"))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "2012882227").split()))
