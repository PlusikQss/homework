from unittest.mock import patch

import pytest

from src.external_api import convert_to_rub


class TestConvertToRub:

    def test_convert_rub_to_rub(self) -> None:
        """Проверяет конвертацию рублей в рубли."""
        transaction = {
            "operationAmount": {
                "amount": "100.50",
                "currency": {"code": "RUB"},
            }
        }

        result = convert_to_rub(transaction)
        assert result == 100.50

    def test_convert_usd_to_rub_with_api(self) -> None:
        """Проверяет конвертацию USD в рубли с использованием API."""
        transaction = {
            "operationAmount": {
                "amount": "10.00",
                "currency": {"code": "USD"},
            }
        }

        with patch("src.external_api.os.getenv") as mock_getenv:
            mock_getenv.side_effect = lambda key, default=None: {
                "API_KEY": "test_key",
                "API_URL": "https://api.test.com",
            }.get(key, default)

            with patch("src.external_api.requests.get") as mock_get:
                mock_response = mock_get.return_value
                mock_response.json.return_value = {"result": 750.00}
                mock_response.raise_for_status.return_value = None

                result = convert_to_rub(transaction)

                assert result == 750.00
                mock_get.assert_called_once()
                assert "USD" in mock_get.call_args[0][0]
                assert "RUB" in mock_get.call_args[0][0]

    def test_convert_eur_to_rub_with_api(self) -> None:
        """Проверяет конвертацию EUR в рубли с использованием API."""
        transaction = {
            "operationAmount": {
                "amount": "5.00",
                "currency": {"code": "EUR"},
            }
        }

        with patch("src.external_api.os.getenv") as mock_getenv:
            mock_getenv.side_effect = lambda key, default=None: {
                "API_KEY": "test_key",
                "API_URL": "https://api.test.com",
            }.get(key, default)

            with patch("src.external_api.requests.get") as mock_get:
                mock_response = mock_get.return_value
                mock_response.json.return_value = {"result": 500.00}
                mock_response.raise_for_status.return_value = None

                result = convert_to_rub(transaction)

                assert result == 500.00

    def test_convert_missing_api_key(self) -> None:
        """Проверяет ошибку при отсутствии API_KEY."""
        transaction = {
            "operationAmount": {
                "amount": "10.00",
                "currency": {"code": "USD"},
            }
        }

        with patch("src.external_api.os.getenv", return_value=None):
            with pytest.raises(ValueError):
                convert_to_rub(transaction)

    @pytest.mark.parametrize(
        "amount, currency_code, expected",
        [
            ("100.00", "RUB", 100.00),
            ("50.00", "RUB", 50.00),
            ("0.00", "RUB", 0.00),
        ],
    )
    def test_convert_rub_parametrized(
        self, amount: str, currency_code: str, expected: float
    ) -> None:
        """Параметризованный тест для рублей."""
        transaction = {
            "operationAmount": {
                "amount": amount,
                "currency": {"code": currency_code},
            }
        }

        result = convert_to_rub(transaction)
        assert result == expected
