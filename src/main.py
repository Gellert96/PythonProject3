from pathlib import Path

from src.masks import (
    get_mask_account,
    get_mask_card_number,
)
from src.processing import (
    filter_by_currency,
    filter_by_state,
    process_bank_search,
    sort_by_date,
)
from src.readers import (
    read_csv,
    read_excel,
)
from src.utils import load_operations

BASE_DIR = Path(__file__).resolve().parent.parent


def mask_account_or_card(value: str) -> str:
    """
    Маскирует номер карты или счета.
    """

    if "Счет" in value:
        number = value.split()[-1]

        return f"Счет {get_mask_account(number)}"

    parts = value.split()

    card_number = parts[-1]

    card_name = " ".join(parts[:-1])

    return (
        f"{card_name} "
        f"{get_mask_card_number(card_number)}"
    )


def main() -> None:
    """
    Основная логика программы.
    """

    print(
        "Привет! Добро пожаловать в программу "
        "работы с банковскими транзакциями."
    )

    print(
        "Выберите необходимый пункт меню:\n"
        "1. Получить информацию о транзакциях "
        "из JSON-файла\n"
        "2. Получить информацию о транзакциях "
        "из CSV-файла\n"
        "3. Получить информацию о транзакциях "
        "из XLSX-файла"
    )

    user_choice = input()

    if user_choice == "1":
        print("Для обработки выбран JSON-файл.")

        data = load_operations(
            str(
                BASE_DIR
                / "data"
                / "operations.json"
            )
        )

    elif user_choice == "2":
        print("Для обработки выбран CSV-файл.")

        data = read_csv(
            str(
                BASE_DIR
                / "data"
                / "transactions.csv"
            )
        )

    elif user_choice == "3":
        print("Для обработки выбран XLSX-файл.")

        data = read_excel(
            str(
                BASE_DIR
                / "data"
                / "transactions_excel.xlsx"
            )
        )

    else:
        print("Неверный пункт меню")

        return

    valid_statuses = [
        "EXECUTED",
        "CANCELED",
        "PENDING",
    ]

    while True:
        print(
            "Введите статус, по которому "
            "необходимо выполнить фильтрацию.\n"
            "Доступные для фильтровки статусы: "
            "EXECUTED, CANCELED, PENDING"
        )

        status = input().upper()

        if status in valid_statuses:
            break

        print(f'Статус операции "{status}" недоступен.')

    data = filter_by_state(data, status)

    print(
        f'Операции отфильтрованы '
        f'по статусу "{status}"'
    )

    print("Отсортировать операции по дате? Да/Нет")

    sort_answer = input().lower()

    if sort_answer == "да":
        print(
            "Отсортировать по возрастанию "
            "или по убыванию?"
        )

        order = input().lower()

        reverse = order != "по возрастанию"

        data = sort_by_date(
            data,
            reverse=reverse,
        )

    print(
        "Выводить только рублевые "
        "транзакции? Да/Нет"
    )

    rub_only = input().lower()

    if rub_only == "да":
        data = filter_by_currency(data)

    print(
        "Отфильтровать список транзакций "
        "по определенному слову "
        "в описании? Да/Нет"
    )

    search_answer = input().lower()

    if search_answer == "да":
        print("Введите строку для поиска:")

        search = input()

        data = process_bank_search(
            data,
            search,
        )

    if not data:
        print(
            "Не найдено ни одной транзакции, "
            "подходящей под ваши условия "
            "фильтрации"
        )

        return

    print(
        "Распечатываю итоговый список "
        "транзакций...\n"
    )

    print(
        f"Всего банковских операций "
        f"в выборке: {len(data)}\n"
    )

    for item in data:
        print(item.get("date", "")[:10])

        print(item.get("description", ""))

        from_info = item.get("from", "")

        to_info = item.get("to", "")

        if from_info:
            masked_from = mask_account_or_card(
                from_info
            )

            masked_to = mask_account_or_card(
                to_info
            )

            print(
                f"{masked_from} -> "
                f"{masked_to}"
            )

        else:
            masked_to = mask_account_or_card(
                to_info
            )

            print(masked_to)

        if "operationAmount" in item:
            amount = item["operationAmount"][
                "amount"
            ]

            currency = item["operationAmount"][
                "currency"
            ]["code"]

        else:
            amount = item.get("amount", "")

            currency = item.get(
                "currency_code",
                "",
            )

        print(
            f"Сумма: {amount} "
            f"{currency}\n"
        )


if __name__ == "__main__":
    main()
