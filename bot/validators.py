from bot.config import (
    SUPPORTED_ORDER_TYPES,
    SUPPORTED_SIDES
)

from bot.exceptions import ValidationError


def validate_order(
    symbol,
    side,
    order_type,
    quantity,
    price=None
):
    symbol = symbol.upper()

    if side not in SUPPORTED_SIDES:
        raise ValidationError(
            f"Invalid side: {side}"
        )

    if order_type not in SUPPORTED_ORDER_TYPES:
        raise ValidationError(
            f"Invalid order type: {order_type}"
        )

    if quantity <= 0:
        raise ValidationError(
            "Quantity must be greater than 0"
        )

    if order_type == "LIMIT":

        if price is None:
            raise ValidationError(
                "Price is required for LIMIT order"
            )

        if price <= 0:
            raise ValidationError(
                "Price must be greater than 0"
            )

    return True