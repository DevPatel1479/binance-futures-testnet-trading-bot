import typer

from rich.console import Console
from rich.table import Table
from rich.panel import Panel

from bot.validators import validate_order
from bot.orders import place_order
from bot.utils import format_price

app = typer.Typer()

console = Console()


@app.command()
def place(
     symbol: str = typer.Option(
        ...,
        "--symbol",
        help="Trading symbol"
    ),
     side: str = typer.Option(
        ...,
        "--side",
        help="BUY or SELL"
    ),
     order_type: str = typer.Option(
        ...,
        "--type",
        help="MARKET or LIMIT"
    ),

    quantity: float = typer.Option(
        ...,
        "--quantity",
        help="Order quantity"
    ),

    price: float = typer.Option(
        None,
        "--price",
        help="Price required for LIMIT order"
    )
):

    try:

        validate_order(
            symbol,
            side,
            order_type,
            quantity,
            price
        )

        console.print(
            Panel.fit(
                "⚡ Connecting to Binance Futures Testnet",
                title="Trading Bot"
            )
        )

        request_table = Table(
            title="Order Request Summary"
        )

        request_table.add_column(
            "Field",
            style="cyan"
        )

        request_table.add_column(
            "Value",
            style="green"
        )

        request_table.add_row(
            "Symbol",
            symbol.upper()
        )

        request_table.add_row(
            "Side",
            side
        )

        request_table.add_row(
            "Type",
            order_type
        )

        request_table.add_row(
            "Quantity",
            str(quantity)
        )

        if price:
            request_table.add_row(
                "Price",
                str(price)
            )

        console.print(request_table)
        with console.status(
            "[bold green]Placing order..."
        ):
            

            response = place_order(
                symbol=symbol,
                side=side,
                order_type=order_type,
                quantity=quantity,
                price=price
            )
        
        response_table = Table(
            title="Order Response"
        )

        response_table.add_column(
            "Field",
            style="cyan"
        )

        response_table.add_column(
            "Value",
            style="green"
        )

        response_table.add_row(
            "Order ID",
            str(response.get("orderId"))
        )

        response_table.add_row(
            "Status",
            str(response.get("status"))
        )

        response_table.add_row(
            "Executed Qty",
            str(response.get("executedQty"))
        )

        response_table.add_row(
            "Average Price",
            format_price(
                response.get("avgPrice")
            )
        )

        console.print(response_table)

        console.print(
            Panel.fit(
                "✅ Order placed successfully!",
                title="Success",
                border_style="green"
            )
        )

    except Exception as e:

        console.print(
            Panel.fit(
                f"❌ {str(e)}",
                title="Order Failed",
                border_style="red"
            )
        )


if __name__ == "__main__":
    app()