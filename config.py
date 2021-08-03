from os import getenv

from dotenv import load_dotenv

load_dotenv()
que = {}
SESSION_NAME = getenv("SESSION_NAME", "AQAAjg_nngvg5JUHI_tIjTIFl74Vgexp4PmWGP7iu9SwbWBjTlRzVXdpLyQtooGsI3NXl50JstWuu9VRr8oJT7Keh2giGTwsweIgPt-8-pZL1ik6sXNXatDbXIOlNe3mpMrPwqTiqwU9UgRXtZiuOsqUI5F86aIagXl03Pw-opGA6PzXd3mjFa-9sE_5kxI5DDtAvPRZ0Dshth744zKE0yi8r1yHfavLad7p-z27qj64K2kQZklTjbkjjRip3dR8vJZBqBqXHJpZaYG5K-pLrR0ZFh0Mx8UCx7aaaDL-Y_cdBcLqk3t8DbQGJZsqobjkpOxjTsU7fYzXGTOtSf5Bm1YvdCqCJAA")
BOT_TOKEN = getenv("BOT_TOKEN", "1909102195:AAGeKwinn5v-UqNClO_TjZNciWsu82_H5ZA")
BOT_NAME = getenv("BOT_NAME", "PATRICIA")
admins = {}
API_ID = int(getenv("API_ID", "7159660"))
API_HASH = getenv("API_HASH", "e1d5bfd2975078a56213605ce0d7f550")

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1832447570").split()))
