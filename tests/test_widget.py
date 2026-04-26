import pytest

from src.widget import get_date, mask_account_card

# -------------------------
# mask_account_card
# -------------------------

def test_mask_card():
    result = mask_account_card("Visa Platinum 7000792289606361")
    assert result.startswith("Visa Platinum")
    assert "****" in result


def test_mask_account():
    result = mask_account_card("Счет 73654108430135874305")
    assert result.startswith("Счет")
    assert "**" in result


@pytest.mark.parametrize("input_data", [
    "Visa Classic 1234567812345678",
    "MasterCard 1111222233334444",
])
def test_mask_card_param(input_data):
    result = mask_account_card(input_data)
    assert "*" in result


# -------------------------
# get_date
# -------------------------


def test_get_date_normal():
    assert get_date("2019-07-03T18:35:29.512364") == "03.07.2019"


def test_get_date_another():
    assert get_date("2020-01-01T00:00:00.000000") == "01.01.2020"


def test_get_date_format():
    result = get_date("2022-12-31T23:59:59.999999")
    assert result == "31.12.2022"
