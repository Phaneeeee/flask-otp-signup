import os

# Load from environment variables set in Render
DB_HOST = os.getenv("MYSQL_ADDON_HOST")
DB_PORT = os.getenv("MYSQL_ADDON_PORT")
DB_USER = os.getenv("MYSQL_ADDON_USER")
DB_PASSWORD = os.getenv("MYSQL_ADDON_PASSWORD")
DB_NAME = os.getenv("MYSQL_ADDON_DB")

SQLALCHEMY_DATABASE_URI = (
    f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Email credentials
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
