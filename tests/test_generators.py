from typing import Any, Dict, List

import pytest

from src.generators import (
    card_number_generator,
    filter_by_currency,
    transaction_descriptions,
)


class TestFilterByCurrency:

    @pytest.mark.parametrize(
        "currency_code, expected_count",
        [
            ("USD", 2),
            ("RUB", 1),
        ],
    )
    def test_filter_by_currency_valid(
        self,
        transactions: List[Dict[str, Any]],
        currency_code: str,
        expected_count: int,
    ) -> None:
        """Проверяет фильтрацию по валюте с разными кодами."""
        result = list(filter_by_currency(transactions, currency_code))
        assert len(result) == expected_count
        assert all(
            item["operationAmount"]["currency"]["code"] == currency_code
            for item in result
        )

    def test_filter_by_currency_empty_list(self) -> None:
        """Проверяет работу с пустым списком."""
        result = list(filter_by_currency([], "USD"))
        assert result == []

    def test_filter_by_currency_no_match(
        self, transactions: List[Dict[str, Any]]
    ) -> None:
        """Проверяет случай, когда валюта не найдена."""
        result = list(filter_by_currency(transactions, "EUR"))
        assert result == []

    def test_filter_by_currency_returns_iterator(
        self, transactions: List[Dict[str, Any]]
    ) -> None:
        """Проверяет, что возвращается итератор."""
        result = filter_by_currency(transactions, "USD")
        assert hasattr(result, "__iter__")
        assert hasattr(result, "__next__")


class TestTransactionDescriptions:

    def test_transaction_descriptions_valid(
        self, transactions: List[Dict[str, Any]]
    ) -> None:
        """Проверяет корректность описаний."""
        result = list(transaction_descriptions(transactions))
        assert result == [
            "Перевод организации",
            "Перевод со счета на счет",
            "Перевод со счета на счет",
        ]

    def test_transaction_descriptions_empty_list(self) -> None:
        """Проверяет работу с пустым списком."""
        result = list(transaction_descriptions([]))
        assert result == []

    @pytest.mark.parametrize(
        "transactions_input, expected",
        [
            (
                [{"description": "Операция 1"}, {"description": "Операция 2"}],
                ["Операция 1", "Операция 2"],
            ),
            (
                [{"description": "Только одна"}],
                ["Только одна"],
            ),
        ],
    )
    def test_transaction_descriptions_parametrized(
        self,
        transactions_input: List[Dict[str, Any]],
        expected: List[str],
    ) -> None:
        """Параметризованный тест для разных входных данных."""
        result = list(transaction_descriptions(transactions_input))
        assert result == expected


class TestCardNumberGenerator:

    @pytest.mark.parametrize(
        "start, stop, expected",
        [
            (
                1,
                5,
                [
                    "0000 0000 0000 0001",
                    "0000 0000 0000 0002",
                    "0000 0000 0000 0003",
                    "0000 0000 0000 0004",
                    "0000 0000 0000 0005",
                ],
            ),
            (
                9999,
                10001,
                [
                    "0000 0000 0000 9999",
                    "0000 0000 0001 0000",
                    "0000 0000 0001 0001",
                ],
            ),
            (1, 1, ["0000 0000 0000 0001"]),
            (9999999999999999, 9999999999999999, ["9999 9999 9999 9999"]),
        ],
    )
    def test_card_number_generator(
        self, start: int, stop: int, expected: List[str]
    ) -> None:
        """Параметризованный тест для разных диапазонов."""
        result = list(card_number_generator(start, stop))
        assert result == expected

    def test_card_number_generator_format(self) -> None:
        """Проверяет формат вывода."""
        numbers = list(card_number_generator(1, 3))
        for number in numbers:
            # Проверяем длину строки: 19 символов (16 цифр + 3 пробела)
            assert len(number) == 19
            # Проверяем, что все блоки по 4 цифры
            blocks = number.split()
            assert len(blocks) == 4
            for block in blocks:
                assert len(block) == 4
                assert block.isdigit()

    def test_card_number_generator_returns_iterator(self) -> None:
        """Проверяет, что возвращается генератор."""
        result = card_number_generator(1, 5)
        assert hasattr(result, "__iter__")
        assert hasattr(result, "__next__")
