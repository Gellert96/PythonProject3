from src.processing import process_bank_search
from src.utils import load_operations


def main() -> None:
    """
    Основная функция программы.
    """
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")

    data = load_operations("data/operations.json")

    search = input("Введите строку для поиска: ")

    result = process_bank_search(data, search)

    if result:
        print(f"Найдено операций: {len(result)}")

        for operation in result:
            print(operation.get("description"))
    else:
        print("Не найдено ни одной транзакции")


if __name__ == "__main__":
    main()
