import os
from typing import Any

import requests


def convert_to_rub(transaction: dict[str, Any]) -> float:
    """Конвертирует сумму транзакции в рубли."""

    amount = float(transaction["operationAmount"]["amount"])
    currency = transaction["operationAmount"]["currency"]["code"]

    if currency == "RUB":
        return amount

    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API key not set")

    url = "https://api.apilayer.com/exchangerates_data/latest"

    response = requests.get(
        url,
        headers={"apikey": api_key},
        params={"base": currency, "symbols": "RUB"},
    )

    data: dict[str, Any] = response.json()

    rate = float(data["rates"]["RUB"])

    return amount * rate
