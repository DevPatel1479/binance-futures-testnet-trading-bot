import logging
import os

os.makedirs("logs", exist_ok=True)

LOG_FORMAT = (
    "%(asctime)s | %(levelname)s | %(message)s"
)

logging.basicConfig(
    filename="logs/trading_bot.log",
    level=logging.INFO,
    format=LOG_FORMAT
)

logger = logging.getLogger("trading_bot")