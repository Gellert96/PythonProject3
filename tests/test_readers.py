from unittest.mock import patch

import pandas as pd

from src.readers import read_csv, read_excel


@patch("src.readers.pd.read_csv")
def test_read_csv(mock_read_csv):
    mock_data = pd.DataFrame(
        [
            {"id": 1, "amount": 100},
            {"id": 2, "amount": 200},
        ]
    )

    mock_read_csv.return_value = mock_data

    result = read_csv("test.csv")

    assert result == [
        {"id": 1, "amount": 100},
        {"id": 2, "amount": 200},
    ]


@patch("src.readers.pd.read_excel")
def test_read_excel(mock_read_excel):
    mock_data = pd.DataFrame(
        [
            {"id": 1, "amount": 300},
            {"id": 2, "amount": 400},
        ]
    )

    mock_read_excel.return_value = mock_data

    result = read_excel("test.xlsx")

    assert result == [
        {"id": 1, "amount": 300},
        {"id": 2, "amount": 400},
    ]
