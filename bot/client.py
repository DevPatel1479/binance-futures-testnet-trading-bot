from binance.client import Client
from bot.config import API_KEY, API_SECRET

client = Client(
    API_KEY,
    API_SECRET
)

# Binance Futures Testnet Endpoint
client.FUTURES_URL = (
    "https://testnet.binancefuture.com/fapi"
)