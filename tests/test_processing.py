import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.fixture
def sample_data():
    return [
        {"id": 1, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 2, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 3, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_filter_by_state_default(sample_data):
    result = filter_by_state(sample_data)
    assert len(result) == 2


@pytest.mark.parametrize("state, expected", [
    ("EXECUTED", 2),
    ("CANCELED", 1),
    ("NONE", 0),
])
def test_filter_by_state_param(sample_data, state, expected):
    result = filter_by_state(sample_data, state)
    assert len(result) == expected


def test_sort_desc(sample_data):
    result = sort_by_date(sample_data)
    dates = [x["date"] for x in result]
    assert dates == sorted(dates, reverse=True)


def test_sort_asc(sample_data):
    result = sort_by_date(sample_data, reverse=False)
    dates = [x["date"] for x in result]
    assert dates == sorted(dates)
