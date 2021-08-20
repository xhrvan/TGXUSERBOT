import logging

from smartbot.main_startup import mongo_client
from smartbot.main_startup.config_var import Config

db_x = mongo_client["LEGEND"]
