# Binance Futures Testnet Trading Bot

A professional Python CLI trading bot built for Binance Futures Testnet (USDT-M) that supports MARKET and LIMIT orders with structured architecture, validation, logging, and enhanced CLI UX.

---

# Features

✅ Place MARKET orders  
✅ Place LIMIT orders  
✅ BUY and SELL support  
✅ Binance Futures Testnet integration  
✅ CLI-based order placement using Typer  
✅ Rich terminal UI using Rich  
✅ Input validation  
✅ Exception handling  
✅ Structured project architecture  
✅ Logging of API requests, responses, and errors  
✅ Environment variable configuration using `.env`

---

# Tech Stack

| Technology | Usage |
|---|---|
| Python 3 | Core language |
| python-binance | Binance Futures API |
| Typer | CLI framework |
| Rich | Beautiful terminal UI |
| Pydantic | Validation |
| python-dotenv | Environment management |

---

# Project Structure

```text
binance-futures-testnet-trading-bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── config.py
│   ├── exceptions.py
│   ├── logger.py
│   ├── models.py
│   ├── orders.py
│   ├── validators.py
│   └── utils.py
│
├── logs/
│   └── trading_bot.log
│
├── screenshots/
│   ├── market_order.png
│   ├── limit_order.png
│   ├── validation_error.png
│   ├── missing_price.png
│   ├── help_command.png
│   └── logs.png
│
├── .env
├── .gitignore
├── cli.py
├── README.md
└── requirements.txt
```

---

# Setup Instructions

## 1. Clone Repository

```bash
git clone <your_github_repository_url>
```

---

## 2. Move Into Project Directory

```bash
cd binance-futures-testnet-trading-bot
```

---

## 3. Create Virtual Environment

```bash
python -m venv venv
```

---

## 4. Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

---

## 5. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Binance Futures Testnet Setup

## Create Binance Futures Testnet Account

Official Testnet:

https://testnet.binancefuture.com

Generate:
- API Key
- Secret Key

---

# Environment Variables

Create a `.env` file in the project root.

## Example

```env
API_KEY=your_api_key
API_SECRET=your_secret_key

BASE_URL=https://testnet.binancefuture.com
USE_TESTNET=True
```

---

# Running The Application

---

# MARKET Order Example

## BUY MARKET Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

---

## SELL MARKET Order

```bash
python cli.py --symbol BTCUSDT --side SELL --type MARKET --quantity 0.001
```

---

# LIMIT Order Example

## BUY LIMIT Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.001 --price 65000
```

---

## SELL LIMIT Order

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 80000
```

---

# Validation Examples

## Invalid Side

```bash
python cli.py --symbol BTCUSDT --side TEST --type MARKET --quantity 0.001
```

### Expected Output

```text
❌ Error: Invalid side: TEST
```

---

## Missing Price For LIMIT Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.001
```

### Expected Output

```text
❌ Error: Price is required for LIMIT order
```

---

# CLI Help Command

```bash
python cli.py --help
```

---

# Example Successful Output

```text
╭────────────── Trading Bot ───────────────╮
│ ⚡ Connecting to Binance Futures Testnet │
╰──────────────────────────────────────────╯

Order Request Summary

┏━━━━━━━━━━┳━━━━━━━━━┓
┃ Field    ┃ Value   ┃
┡━━━━━━━━━━╇━━━━━━━━━┩
│ Symbol   │ BTCUSDT │
│ Side     │ BUY     │
│ Type     │ MARKET  │
│ Quantity │ 0.001   │
└──────────┴─────────┘

Order Response

┏━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━┓
┃ Field         ┃ Value       ┃
┡━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━┩
│ Order ID      │ 123456789   │
│ Status        │ FILLED      │
│ Executed Qty  │ 0.001       │
│ Average Price │ 73500       │
└───────────────┴─────────────┘

✅ Order placed successfully!
```

---

# Logging

All API requests, responses, and errors are logged inside:

```text
logs/trading_bot.log
```

---

# Example Log Output

```text
2026-05-20 20:10:11 | INFO | ORDER REQUEST:
{
  "symbol": "BTCUSDT",
  "side": "BUY",
  "type": "MARKET",
  "quantity": 0.001
}

2026-05-20 20:10:12 | INFO | ORDER RESPONSE:
{
  "orderId": 123456789
}

2026-05-20 20:15:40 | ERROR | ORDER ERROR:
Invalid side: TEST
```

---

# Error Handling

The application handles:

- Invalid order type
- Invalid side
- Missing LIMIT price
- Binance API errors
- Network/API failures
- Invalid quantity input

---

# Enhanced CLI UX (Bonus Feature)

Implemented bonus feature:
- Enhanced CLI User Experience using Rich

Includes:
- Rich tables
- Styled terminal panels
- Colored outputs
- Structured order summaries
- Professional terminal formatting

---

# Assumptions

- User has a valid Binance Futures Testnet account
- API credentials are active
- User has sufficient testnet balance
- Binance Futures Testnet endpoint is available
- Quantity and price comply with Binance trading rules

---

# Screenshots

Screenshots included inside:

```text
screenshots/
```

Contains:
- Successful MARKET order
- Successful LIMIT order
- Validation error
- CLI help command
- Log output

---

# Requirements

```text
python-binance==1.0.36
python-dotenv==1.2.2
typer==0.25.1
rich==15.0.0
pydantic==2.13.4
```

---

# Evaluation Criteria Covered

✅ Correct Binance Futures Testnet integration  
✅ MARKET and LIMIT order support  
✅ BUY and SELL support  
✅ Structured architecture  
✅ Validation and exception handling  
✅ Logging implementation  
✅ Professional CLI UX  
✅ Clear README documentation  

---

# Author

Dev Patel

```