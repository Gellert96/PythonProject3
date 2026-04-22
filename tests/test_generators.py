import pytest

from src.generators import (
    card_number_generator,
    filter_by_currency,
    transaction_descriptions,
)


@pytest.fixture
def sample_transactions():
    return [
        {
            "operationAmount": {"currency": {"code": "USD"}},
            "description": "USD transaction",
        },
        {
            "operationAmount": {"currency": {"code": "RUB"}},
            "description": "RUB transaction",
        },
    ]


def test_filter_by_currency(sample_transactions):
    result = list(filter_by_currency(sample_transactions, "USD"))
    assert len(result) == 1
    assert result[0]["description"] == "USD transaction"


def test_filter_no_results(sample_transactions):
    result = list(filter_by_currency(sample_transactions, "EUR"))
    assert result == []


def test_empty_transactions():
    result = list(filter_by_currency([], "USD"))
    assert result == []


def test_transaction_descriptions(sample_transactions):
    result = list(transaction_descriptions(sample_transactions))
    assert result == ["USD transaction", "RUB transaction"]


def test_transaction_descriptions_empty():
    result = list(transaction_descriptions([]))
    assert result == []


def test_card_number_generator():
    gen = card_number_generator(1, 3)
    result = list(gen)

    assert result == [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
    ]


def test_card_number_format():
    gen = card_number_generator(1, 1)
    number = next(gen)

    assert len(number) == 19
    assert number.count(" ") == 3
