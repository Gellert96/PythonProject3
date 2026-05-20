import re
from collections import Counter
from typing import Any


def filter_by_state(
    data: list[dict[str, Any]],
    state: str = "EXECUTED"
) -> list[dict[str, Any]]:
    """
    Фильтрует список словарей по статусу.
    """
    return [item for item in data if item.get("state") == state]


def sort_by_date(
    data: list[dict[str, Any]],
    reverse: bool = True
) -> list[dict[str, Any]]:
    """
    Сортирует операции по дате.
    """
    return sorted(data, key=lambda x: x["date"], reverse=reverse)


def process_bank_search(
    data: list[dict[str, Any]],
    search: str
) -> list[dict[str, Any]]:
    """
    Ищет операции по строке в описании.
    """
    pattern = re.compile(search, re.IGNORECASE)

    return [
        item for item in data
        if pattern.search(item.get("description", ""))
    ]


def process_bank_operations(
    data: list[dict[str, Any]],
    categories: list[str]
) -> dict[str, int]:
    """
    Подсчитывает количество операций по категориям.
    """
    descriptions = [
        item.get("description", "")
        for item in data
    ]

    counter = Counter(descriptions)

    return {
        category: counter.get(category, 0)
        for category in categories
    }
