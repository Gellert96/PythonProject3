# Bank Operations Widget

## Описание
Проект предназначен для обработки банковских операций клиента.

Основные функции проекта:
- фильтрация операций по статусу
- сортировка операций по дате

---

## Функциональность

### filter_by_state

Фильтрует список банковских операций по значению ключа `state`.

#### Пример:

```python
from src.processing.processing import filter_by_state

data = [
    {"id": 1, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 2, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
]

result = filter_by_state(data, "EXECUTED")
print(result)