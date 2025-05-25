import os

DB_CONFIG = {
    'host': os.environ.get('DB_HOST', 'localhost'),
    'user': os.environ.get('DB_USER', 'root'),
    'password': os.environ.get('DB_PASSWORD', ''),
    'database': os.environ.get('DB_NAME', 'user_auth_db')
}

EMAIL_CONFIG = {
    'EMAIL_ADDRESS': os.environ.get('EMAIL_ADDRESS'),
    'EMAIL_PASSWORD': os.environ.get('EMAIL_PASSWORD')
}
