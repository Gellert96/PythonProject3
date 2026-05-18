import re
from collections import Counter
from typing import Any


def filter_by_state(
    data: list[dict[str, Any]],
    state: str = "EXECUTED"
) -> list[dict[str, Any]]:
    """
    Фильтрует список словарей по значению ключа state.

    :param data: список словарей с банковскими операциями
    :param state: статус операции
    :return: отфильтрованный список
    """
    return [item for item in data if item.get("state") == state]


def sort_by_date(
    data: list[dict[str, Any]],
    reverse: bool = True
) -> list[dict[str, Any]]:
    """
    Сортирует список словарей по дате.

    :param data: список словарей
    :param reverse: порядок сортировки
    :return: отсортированный список
    """
    return sorted(data, key=lambda x: x["date"], reverse=reverse)


def process_bank_search(
    data: list[dict[str, Any]],
    search: str
) -> list[dict[str, Any]]:
    """
    Ищет операции по строке в description.

    :param data: список транзакций
    :param search: строка поиска
    :return: список подходящих операций
    """
    pattern = re.compile(search, re.IGNORECASE)

    return [
        operation
        for operation in data
        if pattern.search(operation.get("description", ""))
    ]


def process_bank_operations(
    data: list[dict[str, Any]],
    categories: list[str]
) -> dict[str, int]:
    """
    Подсчитывает количество операций по категориям.

    :param data: список транзакций
    :param categories: список категорий
    :return: словарь с количеством операций
    """
    descriptions = [
        operation.get("description", "")
        for operation in data
        if operation.get("description", "") in categories
    ]

    return dict(Counter(descriptions))
