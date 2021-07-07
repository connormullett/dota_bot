from enum import Enum
import logging


DEFAULT_LOG_LEVEL = "debug"


USER_NOT_REGISTERED_MESSAGE = "I couldn't find that Telegram username\! Please make sure to register your friend ID using `/register <your friend ID>`"

BAD_RESPONSE_MESSAGE = "Something went wrong, I didn't get a good response :("

MISSING_HERO_ARGUMENT_MESSAGE = "No arguments were given\! Make sure to send a hero name after the command\. Use /help for help"

HERO_NOT_FOUND_MESSAGE = "I couldn't find a hero by the name %s D:"


HELP_TEXT = """
    *Commands*
    `\/register <your steam friend id here>` :: Register your telegram handle to your steam friend id for look ups\. Example :: `\/register 55678920`\n
    `\/help` :: Display this help message\n
    `\/status` :: Check to see if services are running, `OK` means everything is good to go\n
    `\/recents <user:optional> <limit:optional>` :: Look up someone's most recent matches\. Defaults to 5 if limit is not defined and to you if user is not defined\. Must have account id registered using `/register`\. Example :: `\/recents`, `\/recents 10` for 10 most recent matches, `\/recents danvb` for Daniel's last games, `\/recents 20 KittyKirov` for Kirov's last 20 games\n
    `\/match <match_id>` :: Get detailed stats about the outcome of a match\n
    `\/lastmatch <user:optional>` :: Gets the last match someone played\. Defaults to you if no argument is given\. User must be registered for this to work \n
    `\/rank <user:optional>` :: Gets a user's current medal\. Defaults to you if no argument is given\. User must be registered for this to work \n
    `\/winrate <user:optional> <hero name>` :: Gets your or someone else's winrate with the given hero\. User must be registered for this to work\n
    `\/profile <user:optional>` :: Get a link to your or someone else's steam profile\n
    `\/build <hero name or alias>` :: Get recommended items throughout different phases of the game\n
    `\/alias <hero name>` :: Get aliases for a hero\n
    `\/counters <hero name>` :: Get a list of heroes that counter the given hero\. Includes win rates and the percent disadvantage\n
    """

WEBSCRAPER_USER_AGENT_HEADER = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36"
}


class API_URI_ENDPOINTS(Enum):
    HEALTH_CHECK = "health"
    MATCHES = "matches/%s"
    PLAYERS = "players/%s"
    PLAYERS_BY_RANK = "playersByRank"
    PLAYERS_BY_ACCOUNT_ID = "players/%s"
    HERO_STATS = "heroStats"
    CONSTANTS = "constants/%s"
    PLAYER_RECENTS_BY_ACCOUNT_ID = "players/%s/recentMatches"
    PLAYER_MATCHES_BY_HERO = "players/%s/matches?hero_id=%s"
    PLAYER_HERO_STATS = "players/%s/heroes"
    HERO_ITEM_POPULARITY = "heroes/%s/itemPopularity"


class WEB_SCRAPER_URIS(Enum):
    COUNTERS = "https://www.dotabuff.com/heroes/%s/counters"


class QUERY_PARAMETERS(Enum):
    RESPONSE_LIMIT = 5


class HTTP_STATUS_CODES(Enum):
    OK = 200
    NOT_FOUND = 404
    BAD_REQUEST = 400


LOG_LEVEL_MAP = {
    "info": logging.INFO,
    "warning": logging.WARNING,
    "error": logging.ERROR,
    "critical": logging.CRITICAL,
    "debug": logging.DEBUG,
}


JSON_CONSTANT_DATA_FILE_DIR = "src/constant_data/"


class JSON_CONSTANT_DATA_FILE_MAPPING(Enum):
    HERO_DATA = "heroes.json"
    HERO_ALIASES = "aliases.json"


ENVIRONMENT_VARIABLES_CONFIG = {
    "OPEN_DOTA_API_BASE_URL": {
        "required": True,
        "description": "Base URL for hitting the API endpoints",
    },
    "TELEGRAM_BOT_TOKEN": {
        "required": True,
        "description": "Telegram bot token, can be used for local development",
    },
    "LOG_LEVEL": {
        "required": False,
        "description": "Logging level. Defaults to `debug`",
    },
    "POSTGRES_PASSWORD": {
        "required": True,
        "description": "Password for dockerized postgres instance",
    },
    "POSTGRES_USER": {
        "required": True,
        "description": "User name for dockerized postgres instance",
    },
    "POSTGRES_DB": {
        "required": True,
        "description": "Name of dockerized postgres database",
    },
    "DATABASE_PORT": {
        "required": False,
        "description": "Port to use for dockerized postgres container. Defaults to 5432",
    },
}

LOBBY_TYPE_MAP = {
    0: "Normal",
    1: "Practice",
    2: "Tournament",
    3: "Tutorial",
    4: "Coop bots",
    5: "Ranked Teams",
    6: "Ranked Solo",
    7: "Ranked",
    8: "1v1 Mid",
    9: "Battle Cup",
    12: "Nemistice"
}

GAME_MODE_MAP = {
    0: "Unkown",
    1: "All Pick",
    2: "Captains Mode",
    3: "Random Draft",
    4: "Single Draft",
    5: "All Random",
    6: "Into",
    7: "Diretide",
    8: "Reverse Captains Mode",
    9: "Greeviling",
    10: "Tutorial",
    11: "Mid Only",
    12: "Least Played",
    13: "Limited Heroes",
    14: "Compendium Matchmaking",
    15: "Custom",
    16: "Captains Draft",
    17: "Balanced Draft",
    18: "Ability Draft",
    19: "Event",
    20: "All Random Deathmatch",
    21: "1v1 Mid",
    22: "All Draft",
    23: "Turbo",
    24: "Mutation",
}

RANKS = {
    1: "Herald",
    2: "Guardian",
    3: "Crusader",
    4: "Archon",
    5: "Legend",
    6: "Ancient",
    7: "Divine",
}
