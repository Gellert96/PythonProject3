from typing import Any
import os

import requests


def convert_to_rub(transaction: dict[str, Any]) -> float:
    """Конвертирует сумму транзакции в рубли через API."""

    amount = float(transaction["operationAmount"]["amount"])
    currency = transaction["operationAmount"]["currency"]["code"]

    if currency == "RUB":
        return amount

    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API key not set")

    url = "https://api.apilayer.com/exchangerates_data/convert"

    response = requests.get(
        url,
        headers={"apikey": api_key},
        params={
            "from": currency,
            "to": "RUB",
            "amount": amount,
        },
    )

    data: dict[str, Any] = response.json()

    result = float(data["result"])

    return result
