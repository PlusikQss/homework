from typing import Any, Dict, List

import pytest

from src.processing import filter_by_state, sort_by_date


class TestProcessing:

    @pytest.mark.parametrize(
        "state, expected_count",
        [
            ("EXECUTED", 3),
            ("CANCELED", 2),
        ],
    )
    def test_filter_by_state(
        self, sample_operations: List[Dict[str, Any]], state: str, expected_count: int
    ) -> None:
        result = filter_by_state(sample_operations, state)
        assert len(result) == expected_count
        assert all(op["state"] == state for op in result)

    def test_filter_by_state_default(
        self, sample_operations: List[Dict[str, Any]]
    ) -> None:
        result = filter_by_state(sample_operations)
        assert all(op["state"] == "EXECUTED" for op in result)

    def test_filter_by_state_no_match(
        self, sample_operations: List[Dict[str, Any]]
    ) -> None:
        result = filter_by_state(sample_operations, "PENDING")
        assert result == []

    def test_sort_by_date_desc(self, sample_operations: List[Dict[str, Any]]) -> None:
        result = sort_by_date(sample_operations, reverse=True)
        assert result[0]["date"] == "2024-07-10T18:45:00"

    def test_sort_by_date_asc(self, sample_operations: List[Dict[str, Any]]) -> None:
        result = sort_by_date(sample_operations, reverse=False)
        assert result[0]["date"] == "2024-04-01T08:00:00"

    def test_sort_by_date_same_dates(self) -> None:
        operations = [
            {"id": 1, "date": "2024-01-01T12:00:00"},
            {"id": 2, "date": "2024-01-01T12:00:00"},
        ]
        result = sort_by_date(operations)
        assert result[0]["id"] == 1
        assert result[1]["id"] == 2
