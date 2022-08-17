# (c) @PredatorHackerzZ

import os


class Config(object):
    API_ID = int(os.environ.get("API_ID", 12345))
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    BOT_SESSION_NAME = os.environ.get("BOT_SESSION_NAME", "PHListBot")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", "")
    CHANNEL_ID = int(os.environ.get("CHANNEL_ID", -100))
    BOT_USERNAME = os.environ.get("BOT_USERNAME")
    BOT_OWNER = int(os.environ.get("BOT_OWNER"))
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", None)
    LOG_CHANNEL = os.environ.get("LOG_CHANNEL", None)
    ABOUT_BOT_TEXT = """<b>This Is a Simple Message Search bot by @DTG_TV & @DTG_BOTS.

🤖 My Name: <a href='https://t.me/DTG_TV'> Me Nahi Bataunga😂😂 </a>

📝 Language : <a href='https://www.python.org'> Python V3</a>

📚 Library: <a href='https://docs.pyrogram.org'> Pyrogram </a>

📡 Server: <a href='https://heroku.com'> Heroku </a>

👨‍💻 Modified By: <a href='https://t.me/DTG_BOTS'> Let's Play Hide & Seek (❁´◡`❁) </a>

🌀 Github Repo: <a href='https://github.com/PredatorHackerzZ/MessageSearchBot'>Agar Mera Wala Chahiye To 2k karao Varna Isise Kam Chalao</a>

👥 Bots Support: <a href='https://t.me/DTG_SUPPORT'> Aapke Liye Ye Banda Hazir Hai </a>

📢 Bots Updates: <a href='https://t.me/DTG_BOTS'> Click Karo Or Join Karo </a></b>
"""
    
    ABOUT_HELP_TEXT =  """<b>👨‍💻 Developer : <a href='https://t.me/DTG_Admin_bot'>DTG TV</a>
If You Want Your Own Bot Like This Then You Can Contact Our Developer.</b>
"""
    
    HOME_TEXT = """
<b>Hey! {}❤️,
I'm Mdisk Search Robot.🤖</a>
I Can Search!🔍 What You Want?😜
<a>Deploy ❤ By @DTG_TV</a></b>
"""


    START_MSG = """
<b>Hey! {}❤️,
I'm Mdisk Search Robot.🤖</a>
I Can Search!🔍 What You Want?😜
You Can Add Me In Your Groups
<a>Deploy ❤ By @DTG_TV</a></b>
"""
