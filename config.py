"""Configuration file for API keys"""
import os # for environment variables
from dotenv import load_dotenv  # load environment variables from .env file

load_dotenv()

YANDEX_IAM_TOKEN = os.getenv('YANDEX_IAM_TOKEN')
YANDEX_FOLDER_ID = os.getenv('YANDEX_FOLDER_ID')
YANDEX_SPEECHKIT_API_KEY = os.getenv('YANDEX_SPEECHKIT_API_KEY')
