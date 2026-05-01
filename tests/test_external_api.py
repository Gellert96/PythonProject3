from unittest.mock import patch


from src.external_api import convert_to_rub


@patch("src.external_api.requests.get")
@patch("src.external_api.os.getenv")
def test_usd_conversion(mock_getenv, mock_get):
    mock_getenv.return_value = "test_api_key"

    mock_get.return_value.json.return_value = {
        "result": 1000.0
    }

    transaction = {
        "operationAmount": {
            "amount": "10",
            "currency": {"code": "USD"}
        }
    }

    result = convert_to_rub(transaction)

    assert result == 1000.0
