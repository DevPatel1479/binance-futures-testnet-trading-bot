class ValidationError(Exception):
    """Raised for invalid user input."""
    pass


class BinanceOrderError(Exception):
    """Raised when Binance API fails."""
    pass