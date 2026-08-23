from typing import Any, Dict, List

import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


class TestGenerators:

    def test_filter_by_currency_usd(self, transactions: List[Dict[str, Any]]) -> None:
        result = list(filter_by_currency(transactions, "USD"))
        assert len(result) == 2
        assert all(
            item["operationAmount"]["currency"]["code"] == "USD"
            for item in result
        )

    def test_filter_by_currency_rub(self, transactions: List[Dict[str, Any]]) -> None:
        result = list(filter_by_currency(transactions, "RUB"))
        assert len(result) == 1
        assert result[0]["operationAmount"]["currency"]["code"] == "RUB"

    def test_filter_by_currency_empty_list(self) -> None:
        result = list(filter_by_currency([], "USD"))
        assert result == []

    def test_filter_by_currency_no_match(self, transactions: List[Dict[str, Any]]) -> None:
        result = list(filter_by_currency(transactions, "EUR"))
        assert result == []

    def test_transaction_descriptions(self, transactions: List[Dict[str, Any]]) -> None:
        descriptions = list(transaction_descriptions(transactions))
        assert descriptions == [
            "Перевод организации",
            "Перевод со счета на счет",
            "Перевод со счета на счет",
        ]

    def test_transaction_descriptions_empty(self) -> None:
        descriptions = list(transaction_descriptions([]))
        assert descriptions == []

    @pytest.mark.parametrize(
        "start, stop, expected",
        [
            (1, 5, [
                "0000 0000 0000 0001",
                "0000 0000 0000 0002",
                "0000 0000 0000 0003",
                "0000 0000 0000 0004",
                "0000 0000 0000 0005",
            ]),
            (9999, 10001, [
                "0000 0000 0000 9999",
                "0000 0000 0001 0000",
                "0000 0000 0001 0001",
            ]),
            (1, 1, ["0000 0000 0000 0001"]),
        ],
    )
    def test_card_number_generator(
        self, start: int, stop: int, expected: List[str]
    ) -> None:
        result = list(card_number_generator(start, stop))
        assert result == expected
