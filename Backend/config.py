import os

DB_CONFIG = {
    "DB_HOST": os.getenv("MYSQL_ADDON_HOST"),
    "DB_PORT": os.getenv("MYSQL_ADDON_PORT"),
    "DB_USER": os.getenv("MYSQL_ADDON_USER"),
    "DB_PASSWORD": os.getenv("MYSQL_ADDON_PASSWORD"),
    "DB_NAME": os.getenv("MYSQL_ADDON_DB")
}

EMAIL_CONFIG = {
    "EMAIL_ADDRESS": os.getenv("EMAIL_ADDRESS"),
    "EMAIL_PASSWORD": os.getenv("EMAIL_PASSWORD")
}
