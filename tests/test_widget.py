import pytest

from src.widget import get_date, mask_account_card


class TestWidget:

    @pytest.mark.parametrize(
        "input_data, expected",
        [
            ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
            ("Счет 73654108430135874305", "Счет **4305"),
            ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
            ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
            ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
        ],
    )
    def test_mask_account_card_valid(self, input_data: str, expected: str) -> None:
        assert mask_account_card(input_data) == expected

    @pytest.mark.parametrize(
        "invalid_input",
        ["", "Счет", "Visa", "Visa 12ab567890123456"],
    )
    def test_mask_account_card_invalid(self, invalid_input: str) -> None:
        with pytest.raises(ValueError):
            mask_account_card(invalid_input)

    @pytest.mark.parametrize(
        "date_string, expected",
        [
            ("2024-03-11T02:26:18.671407", "11.03.2024"),
            ("2023-12-31T23:59:59.999999", "31.12.2023"),
            ("2024-07-10T18:45:00", "10.07.2024"),
        ],
    )
    def test_get_date_valid(self, date_string: str, expected: str) -> None:
        assert get_date(date_string) == expected

    @pytest.mark.parametrize(
        "invalid_date",
        ["", "invalid", "10.12.2024"],
    )
    def test_get_date_invalid(self, invalid_date: str) -> None:
        with pytest.raises(ValueError):
            get_date(invalid_date)
