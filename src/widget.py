from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(data: str) -> str:
    """Маскирует номер карты или счета в строке."""

    parts = data.split()
    number = parts[-1]
    name = " ".join(parts[:-1])

    if name.lower() == "счет":
        return f"{name} {get_mask_account(number)}"

    return f"{name} {get_mask_card_number(number)}"


def get_date(date_str: str) -> str:
    """Преобразует дату в формат ДД.ММ.ГГГГ."""

    date_part = date_str.split("T")[0]
    year, month, day = date_part.split("-")
