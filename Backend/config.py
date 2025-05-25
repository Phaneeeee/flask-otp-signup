import os

DB_CONFIG = {
    'host': os.environ.get('MYSQL_ADDON_HOST'),
    'user': os.environ.get('MYSQL_ADDON_USER'),
    'password': os.environ.get('MYSQL_ADDON_PASSWORD'),
    'database': os.environ.get('MYSQL_ADDON_DB')
}

EMAIL_CONFIG = {
    'EMAIL_ADDRESS': os.environ.get('EMAIL_ADDRESS'),
    'EMAIL_PASSWORD': os.environ.get('EMAIL_PASSWORD')
}
