from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number() -> None:
    # Пример карты
    card_number = "7000792289606361"
    expected = "7000 79** **** 6361"
    assert get_mask_card_number(card_number) == expected

    # Ещё пример
    card_number2 = "1234567890123456"
    expected2 = "1234 56** **** 3456"
    assert get_mask_card_number(card_number2) == expected2


def test_get_mask_account() -> None:
    # Пример счета
    account_number = "73654108430135874305"
    expected = "**4305"
    assert get_mask_account(account_number) == expected

    # Ещё пример
    account_number2 = "12345678"
    expected2 = "**5678"
    assert get_mask_account(account_number2) == expected2
