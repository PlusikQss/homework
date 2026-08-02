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

from src.widget import mask_account_card, get_date

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from src.widget import mask_account_card, get_date

def test_mask_account_card_card():
    result = mask_account_card("Visa Platinum 7000792289606361")
    assert "79** **** 6361" in result
    assert result.startswith("Visa Platinum")

def test_mask_account_card_account():
    result = mask_account_card("Счет 73654108430135874305")
    assert result.startswith("Счет")
    assert "**4305" in result

def test_get_date():
    result = get_date("2024-03-11T02:26:18.671407")
    assert result == "11.03.2024"