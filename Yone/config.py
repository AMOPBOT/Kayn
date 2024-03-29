
import json
import os


def get_user_list(config, key):
    with open("{}/Yone/{}".format(os.getcwd(), config), "r") as json_file:
        return json.load(json_file)[key]

class Config(object):
    LOGGER = True

    API_ID = "12227067"
    API_HASH = "b463bedd791aa733ae2297e6520302fe"
    TOKEN = "2003992067:AAGAxkBGzQS2O_saxexIlurwHfVKtrgdoKU"
    OWNER_ID = "2105971379"
    OWNER_USERNAME = "sultan11100"
    SUPPORT_CHAT = "Yone_Support"
    JOIN_LOGGER = "-1001841879487"
    EVENT_LOGS = "-1001841879487"
    DEEP_API = "c8e3d7fc-1f7e-455b-8019-5c1b7f21047a"
    OPENAI_KEY = ""
    BOT_USERNAME = "Kayn_Robot"
    BOT_NAME = "Kayn"
    # 
    # DATABASE_URL = "postgres://ixweewbx:9OoB_feF6d6wK1W4YycgwHzRHQXezsNA@arjuna.db.elephantsql.com/ixweewbx"  # sql
    DATABASE_URL = "postgres://sywquewx:UQRTM7m32oEOURHxuEFw6SX4hH2SQe9j@peanut.db.elephantsql.com/sywquewx"  # sql
    LOAD = []
    NO_LOAD = []
    WEBHOOK = False
    REDIS_URL = "redis://default:725m47dhlmisA0QecURSMkcHNGXkM1uP@redis-15808.c275.us-east-1-4.ec2.cloud.redislabs.com:15808"

    INSPECTOR = get_user_list("elevated_users.json", "ins")
    DEV_USERS = get_user_list("elevated_users.json", "devs")
    REQUESTER = get_user_list("elevated_users.json", "req")

    CERT_PATH = None
    STRICT_GBAN = True
    PORT = "8080"
    DEL_CMDS = True
    STRICT_GBAN = True
    WORKERS = 20
    ALLOW_EXCL = True
    ALLOW_CHATS = True
    PHOTO = "https://graph.org/file/b29030496d3224d15cb57.jpg" # Miss Poppy Music Pic
    INFOPIC = True


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
