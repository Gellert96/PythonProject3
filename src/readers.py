from typing import Any, cast

import pandas as pd


def read_csv(file_path: str) -> list[dict[str, Any]]:
    """
    Считывает транзакции из CSV-файла.
    """
    data = pd.read_csv(file_path)

    return cast(list[dict[str, Any]], data.to_dict(orient="records"))


def read_excel(file_path: str) -> list[dict[str, Any]]:
    """
    Считывает транзакции из Excel-файла.
    """
    data = pd.read_excel(file_path)

    return cast(list[dict[str, Any]], data.to_dict(orient="records"))
