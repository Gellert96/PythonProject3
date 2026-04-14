from typing import Any, Dict, List


def filter_by_state(
    data: List[Dict[str, Any]],
    state: str = "EXECUTED"
) -> List[Dict[str, Any]]:
    """
    Фильтрует список словарей по значению ключа state.

    :param data: список словарей с банковскими операциями
    :param state: статус операции (по умолчанию 'EXECUTED')
    :return: новый список словарей, отфильтрованный по state
    """
    return [item for item in data if item.get("state") == state]


def sort_by_date(
    data: List[Dict[str, Any]],
    reverse: bool = True
) -> List[Dict[str, Any]]:
    """
    Сортирует список словарей по дате.

    :param data: список словарей с банковскими операциями
    :param reverse: порядок сортировки (True — по убыванию)
    :return: отсортированный список словарей
    """
    return sorted(data, key=lambda x: x["date"], reverse=reverse)
