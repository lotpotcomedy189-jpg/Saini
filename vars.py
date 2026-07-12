#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "34422904"))
API_HASH = environ.get("API_HASH", "7e0002469784f47fc08a6b3d93d7ebed")
BOT_TOKEN = environ.get("BOT_TOKEN", "8641304240:AAHujFxKVS4GsqwLD-7mdu4uRGEk7ae8KFM")
OWNER = int(environ.get("OWNER", "5349573682"))
CREDIT = environ.get("CREDIT", "RADHE RADHE 🍁")
AUTH_USER = os.environ.get('AUTH_USERS', '5349573682').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
