import pytest

from src.widget import get_date, mask_account_card


@pytest.fixture
def operations_data() -> list[dict[str, str]]:
    return [
        {"type": "card", "number": "7000792289606361"},
        {"type": "account", "number": "73654108430135874305"},
        {"type": "unknown", "number": "123"},
    ]


class TestWidget:
    @pytest.mark.parametrize(
        "op, expected",
        [
            ({"type": "card", "number": "7000792289606361"}, "7000 79** **** 6361"),
            ({"type": "account", "number": "73654108430135874305"}, "**4305"),
            ({"type": "unknown", "number": "123"}, None),
        ],
    )
    def test_mask_account_card(
        self,
        op: dict[str, str],
        expected: str | None,
        operations_data: list[dict[str, str]],
    ) -> None:
        _ = operations_data
        result = mask_account_card(op)
        assert result == expected

    @pytest.mark.parametrize(
        "date_str, expected",
        [
            ("2024-12-10", "2024-12-10"),
            ("10.12.2024", "2024-12-10"),
            ("2024/12/10", "2024-12-10"),
            ("", None),
            ("invalid", None),
        ],
    )
    def test_get_date(self, date_str: str | None, expected: str | None) -> None:
        result = get_date(date_str)
        assert result == expected
