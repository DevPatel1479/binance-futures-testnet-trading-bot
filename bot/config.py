import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")

BASE_URL = os.getenv(
    "BASE_URL",
    "https://testnet.binancefuture.com"
)

USE_TESTNET = os.getenv(
    "USE_TESTNET",
    "True"
).lower() == "true"

SUPPORTED_ORDER_TYPES = [
    "MARKET",
    "LIMIT"
]

SUPPORTED_SIDES = [
    "BUY",
    "SELL"
]