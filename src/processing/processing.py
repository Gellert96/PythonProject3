from typing import List, Dict


def filter_by_state(data: List[Dict], state: str = "EXECUTED") -> List[Dict]:
    """ Фильтрует список словарей по значению ключа state.

    :param data: список словарей с банковскими операциями
    :param state: статус операции (по умолчанию 'EXECUTED')
    :return: новый список словарей, отфильтрованный по state """
    return [item for item in data if item.get("state") == state]


def sort_by_date(data: List[Dict], reverse: bool = True) -> List[Dict]:
    """ Сортирует список словарей по дате.

    :param data: список словарей с банковскими операциями
    :param reverse: порядок сортировки (True — по убыванию, False — по возрастанию)
    :return: отсортированный список словарей  """
    return sorted(data, key=lambda x: x.get("date"), reverse=reverse)