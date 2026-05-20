from bot.client import client
from bot.logger import logger
from bot.exceptions import BinanceOrderError

import time


def place_order(
    symbol,
    side,
    order_type,
    quantity,
    price=None
):
    try:

        payload = {
            "symbol": symbol.upper(),
            "side": side,
            "type": order_type,
            "quantity": quantity
        }

        if order_type == "LIMIT":

            payload["price"] = price
            payload["timeInForce"] = "GTC"

        logger.info(
            f"ORDER REQUEST: {payload}"
        )

        response = client.futures_create_order(
            **payload
        )

        logger.info(
            f"INITIAL ORDER RESPONSE: {response}"
        )

        # Wait briefly for Binance to process order
        time.sleep(2)

        try:

            updated_order = client.futures_get_order(
                symbol=symbol.upper(),
                orderId=response["orderId"]
            )

            logger.info(
                f"FINAL ORDER DETAILS: {updated_order}"
            )

            return updated_order

        except Exception:

            # fallback to original response
            return response

    except Exception as e:

        logger.error(
            f"ORDER ERROR: {str(e)}"
        )

        raise BinanceOrderError(str(e))