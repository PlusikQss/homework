import pytest

from src.masks import get_mask_account, get_mask_card_number


class TestMasks:

    @pytest.mark.parametrize(
        "card_number, expected",
        [
            ("7000792289606361", "7000 79** **** 6361"),
            ("1234567890123456", "1234 56** **** 3456"),
            ("4321", "****"),  # меньше 16 цифр
        ],
    )
    def test_get_mask_card_number_valid(self, card_number: str, expected: str) -> None:
        assert get_mask_card_number(card_number) == expected

    @pytest.mark.parametrize(
        "invalid_card",
        ["123", "12a4567890123456", ""],
    )
    def test_get_mask_card_number_invalid(self, invalid_card: str) -> None:
        with pytest.raises(ValueError):
            get_mask_card_number(invalid_card)

    @pytest.mark.parametrize(
        "account_number, expected",
        [
            ("73654108430135874305", "**4305"),
            ("40817810000000000001", "**0001"),
        ],
    )
    def test_get_mask_account_valid(self, account_number: str, expected: str) -> None:
        assert get_mask_account(account_number) == expected

    @pytest.mark.parametrize(
        "invalid_account",
        ["123", "12a4", ""],
    )
    def test_get_mask_account_invalid(self, invalid_account: str) -> None:
        with pytest.raises(ValueError):
            get_mask_account(invalid_account)
