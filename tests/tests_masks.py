import pytest
from src.masks import get_mask_card_number, get_mask_account


class TestGetMakCardNumber:
    def test_valid_card(self):
        assert get_mask_card_number("7000792289606361") == "7000 79** **** 6361"

    def test_another_valid_card(self):
        assert get_mask_card_number("1234567890123456") == "1234 56** **** 3456"

    def test_invalid_length_too_short(self):
        with pytest.raises(ValueError):
            get_mask_card_number("1234567890123")

    def test_invalid_length_too_long(self):
        with pytest.raises(ValueError):
            get_mask_card_number("12345678901234567")

    def test_non_digit_input(self):
        with pytest.raises(ValueError):
            get_mask_card_number("1234abcd90123456")


class TestGetMaskAccount:
    def test_valid_account(self):
        assert get_mask_account("73654108430135874305") == "**4305"

    def test_account_exactly_4_digits(self):
        assert get_mask_account("1234") == "**1234"

    def test_shorter_than_4_raises(self):
        with pytest.raises(ValueError):
            get_mask_account("123")

    def test_non_digit_account_raises(self):
        with pytest.raises(ValueError):
            get_mask_account("12a4")
