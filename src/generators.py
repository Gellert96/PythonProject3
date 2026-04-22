from typing import Any, Dict, Iterator, List


def filter_by_currency(transactions: List[Dict[str, Any]], currency: str) -> Iterator[Dict[str, Any]]:
    for transaction in transactions:
        if transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency:
            yield transaction


def transaction_descriptions(transactions: List[Dict[str, Any]]) -> Iterator[str]:
    for transaction in transactions:
        yield transaction.get("description", "")


def card_number_generator(start: int, end: int) -> Iterator[str]:
    for number in range(start, end + 1):
        card = str(number).zfill(16)
        yield f"{card[0:4]} {card[4:8]} {card[8:12]} {card[12:16]}"
