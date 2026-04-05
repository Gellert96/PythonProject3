def get_mask_card_number(card_number: str) -> str:
    """Маскирует номер банковской карты в формате XXXX XX** **** XXXX"""
    first_six = card_number[:6]
    last_four = card_number[-4:]
    masked = first_six + "**" + "****" + last_four
    return f"{masked[:4]} {masked[4:8]} {masked[8:12]} {masked[12:16]}"


def get_mask_account(account_number: str) -> str:
    """Маскирует номер банковского счета в формате **XXXX"""
    return f"**{account_number[-4:]}"
