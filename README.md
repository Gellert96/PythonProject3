# Bank Operations Widget

## Описание

Проект предназначен для обработки банковских операций клиента.

Основные функции проекта:

* фильтрация операций по статусу
* сортировка операций по дате

---

## Функциональность

### filter_by_state

Фильтрует список банковских операций по значению ключа `state`.

Параметры:

* data — список словарей с операциями
* state — статус операции (по умолчанию "EXECUTED")

Пример:

```
from src.processing import filter_by_state

data = [
    {"id": 1, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 2, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
]

result = filter_by_state(data, "EXECUTED")
print(result)
```

---

### sort_by_date

Сортирует список банковских операций по дате.

Параметры:

* data — список словарей с операциями
* reverse — порядок сортировки:
  True — по убыванию (по умолчанию)
  False — по возрастанию

Пример:

```
from src.processing import sort_by_date

data = [
    {"id": 1, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 2, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
]

result = sort_by_date(data)
print(result)
```
### mask_account_card

Маскирует номер карты или счета.

Пример:

```python
from src.masks import get_mask_card_number, get_mask_account

## Установка

```
git clone https://github.com/Gellert96/PythonProject3.git
cd PythonProject3
```

---

## Использование

```
from src.processing import filter_by_state, sort_by_date

data = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
]

filtered = filter_by_state(data, "EXECUTED")
sorted_data = sort_by_date(data)

print(filtered)
print(sorted_data)
```

---

## Структура проекта

```
src/
  processing.py
  masks.py

main.py
README.md
```


## ТЕСТИРОВАНИЕ 


```md id="tests"
## Тестирование

Проект покрыт тестами с использованием pytest.

### Запуск тестов:

```bash
pytest


---

## Декораторы

### log

Декоратор `log` используется для логирования работы функций.

Он записывает:
- имя функции
- результат выполнения (если успешно)
- информацию об ошибке и входные параметры (если произошла ошибка)

### Параметры

- `filename` (необязательный) — имя файла для записи логов  
  - если указан → лог записывается в файл  
  - если не указан → лог выводится в консоль  

---

### Пример использования

```python
from src.decorators import log

@log()
def add(x, y):
    return x + y

add(1, 2)
add ok