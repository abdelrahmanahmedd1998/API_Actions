import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.environ.get("BASE_URL", "https://www.saucedemo.com/")
API_BASE_URL = os.environ.get("API_BASE_URL", "https://reqres.in")

SAUCE_VALID_USERNAME = os.environ.get("SAUCE_VALID_USERNAME")
SAUCE_LOCKED_USERNAME = os.environ.get("SAUCE_LOCKED_USERNAME")
SAUCE_PASSWORD = os.environ.get("SAUCE_PASSWORD")
