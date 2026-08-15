from typing import Optional

import pytest

from src.widget import get_date, mask_account_card


class TestWidget:
    @pytest.mark.parametrize("input_str, expected_part", [
        ("Visa Platinum 7000792289606361", "79** **** 6361"),
        ("Счет 73654108430135874305", "**4305"),
        ("Карта МИР 1234567890123456", "56** **** 3456"),
    ])
    def test_mask_account_card(self, input_str: str, expected_part: str) -> None:
        result = mask_account_card(input_str)
        prefix = input_str.split()[0]
        assert result.startswith(prefix)
        assert expected_part in result

    @pytest.mark.parametrize("date_input, expected_output", [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2024-05-20 09:30:00", "20.05.2024"),
        ("", ""),
        (None, ""),
    ])
    def test_get_date(self, date_input: Optional[str], expected_output: str) -> None:
        assert get_date(date_input) == expected_output
