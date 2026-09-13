from typing import Any, Dict, List
from unittest.mock import MagicMock, patch

import pandas as pd
import pytest

from src.csv_excel_reader import read_csv_file, read_excel_file


class TestReadCsvFile:

    @patch("src.csv_excel_reader.pd.read_csv")
    def test_read_csv_file_success(self, mock_read_csv: MagicMock) -> None:
        """Проверяет успешное чтение CSV-файла."""
        # Мокаем DataFrame
        mock_df = pd.DataFrame(
            [
                {"id": 1, "amount": "100.00", "currency": "RUB"},
                {"id": 2, "amount": "200.00", "currency": "USD"},
            ]
        )
        mock_read_csv.return_value = mock_df

        result = read_csv_file("test.csv")

        assert len(result) == 2
        assert result[0]["id"] == 1
        assert result[1]["amount"] == "200.00"
        mock_read_csv.assert_called_once_with("test.csv")

    @patch("src.csv_excel_reader.pd.read_csv")
    def test_read_csv_file_not_found(self, mock_read_csv: MagicMock) -> None:
        """Проверяет обработку несуществующего файла."""
        mock_read_csv.side_effect = FileNotFoundError("File not found")

        result = read_csv_file("nonexistent.csv")

        assert result == []

    @patch("src.csv_excel_reader.pd.read_csv")
    def test_read_csv_file_empty(self, mock_read_csv: MagicMock) -> None:
        """Проверяет обработку пустого файла."""
        mock_read_csv.return_value = pd.DataFrame()

        result = read_csv_file("empty.csv")

        assert result == []

    @patch("src.csv_excel_reader.pd.read_csv")
    def test_read_csv_file_error(self, mock_read_csv: MagicMock) -> None:
        """Проверяет обработку ошибок при чтении."""
        mock_read_csv.side_effect = Exception("Some error")

        result = read_csv_file("bad.csv")

        assert result == []

    @pytest.mark.parametrize(
        "mock_data, expected_count",
        [
            ([{"id": 1}], 1),
            ([{"id": 1}, {"id": 2}], 2),
            ([], 0),
        ],
    )
    @patch("src.csv_excel_reader.pd.read_csv")
    def test_read_csv_file_parametrized(
        self,
        mock_read_csv: MagicMock,
        mock_data: List[Dict[str, Any]],
        expected_count: int,
    ) -> None:
        """Параметризованный тест для разных данных."""
        mock_read_csv.return_value = pd.DataFrame(mock_data)

        result = read_csv_file("test.csv")

        assert len(result) == expected_count


class TestReadExcelFile:

    @patch("src.csv_excel_reader.pd.read_excel")
    def test_read_excel_file_success(self, mock_read_excel: MagicMock) -> None:
        """Проверяет успешное чтение Excel-файла."""
        mock_df = pd.DataFrame(
            [
                {"id": 1, "amount": "100.00", "currency": "RUB"},
                {"id": 2, "amount": "200.00", "currency": "USD"},
            ]
        )
        mock_read_excel.return_value = mock_df

        result = read_excel_file("test.xlsx")

        assert len(result) == 2
        assert result[0]["id"] == 1
        assert result[1]["amount"] == "200.00"
        mock_read_excel.assert_called_once_with("test.xlsx")

    @patch("src.csv_excel_reader.pd.read_excel")
    def test_read_excel_file_not_found(self, mock_read_excel: MagicMock) -> None:
        """Проверяет обработку несуществующего файла."""
        mock_read_excel.side_effect = FileNotFoundError("File not found")

        result = read_excel_file("nonexistent.xlsx")

        assert result == []

    @patch("src.csv_excel_reader.pd.read_excel")
    def test_read_excel_file_empty(self, mock_read_excel: MagicMock) -> None:
        """Проверяет обработку пустого файла."""
        mock_read_excel.return_value = pd.DataFrame()

        result = read_excel_file("empty.xlsx")

        assert result == []

    @patch("src.csv_excel_reader.pd.read_excel")
    def test_read_excel_file_error(self, mock_read_excel: MagicMock) -> None:
        """Проверяет обработку ошибок при чтении."""
        mock_read_excel.side_effect = Exception("Some error")

        result = read_excel_file("bad.xlsx")

        assert result == []

    @pytest.mark.parametrize(
        "mock_data, expected_count",
        [
            ([{"id": 1}], 1),
            ([{"id": 1}, {"id": 2}, {"id": 3}], 3),
            ([], 0),
        ],
    )
    @patch("src.csv_excel_reader.pd.read_excel")
    def test_read_excel_file_parametrized(
        self,
        mock_read_excel: MagicMock,
        mock_data: List[Dict[str, Any]],
        expected_count: int,
    ) -> None:
        """Параметризованный тест для разных данных."""
        mock_read_excel.return_value = pd.DataFrame(mock_data)

        result = read_excel_file("test.xlsx")

        assert len(result) == expected_count
