from typing import Any

import pandas as pd


def read_csv_transactions(file_path: str) -> list[dict[str, Any]]:
    """
    Считывает финансовые операции из CSV-файла.

    :param file_path: путь до CSV-файла
    :return: список словарей с транзакциями
    """
    data = pd.read_csv(file_path)

    return data.to_dict(orient="records")


def read_excel_transactions(file_path: str) -> list[dict[str, Any]]:
    """
    Считывает финансовые операции из Excel-файла.

    :param file_path: путь до Excel-файла
    :return: список словарей с транзакциями
    """
    data = pd.read_excel(file_path)

    return data.to_dict(orient="records")
