def format_price(price):
    if price:
        return f"{float(price):,.2f}"

    return "N/A"