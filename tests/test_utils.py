import json
from pathlib import Path
from typing import Any, Dict, List

import pytest

from src.utils import read_json_file


class TestReadJsonFile:

    def test_read_json_file_success(self, tmp_path: Path) -> None:
        """Проверяет успешное чтение JSON-файла."""
        test_data = [{"id": 1, "name": "test"}]
        file_path = tmp_path / "test.json"

        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(test_data, file, ensure_ascii=False)

        result = read_json_file(str(file_path))
        assert result == test_data

    def test_read_json_file_not_found(self) -> None:
        """Проверяет обработку несуществующего файла."""
        result = read_json_file("nonexistent.json")
        assert result == []

    def test_read_json_file_empty(self, tmp_path: Path) -> None:
        """Проверяет обработку пустого файла."""
        file_path = tmp_path / "empty.json"
        file_path.write_text("", encoding="utf-8")

        result = read_json_file(str(file_path))
        assert result == []

    def test_read_json_file_not_list(self, tmp_path: Path) -> None:
        """Проверяет обработку файла с не-списком."""
        file_path = tmp_path / "not_list.json"
        file_path.write_text('{"key": "value"}', encoding="utf-8")

        result = read_json_file(str(file_path))
        assert result == []

    def test_read_json_file_invalid_json(self, tmp_path: Path) -> None:
        """Проверяет обработку файла с некорректным JSON."""
        file_path = tmp_path / "invalid.json"
        file_path.write_text("invalid json", encoding="utf-8")

        result = read_json_file(str(file_path))
        assert result == []

    @pytest.mark.parametrize(
        "content, expected",
        [
            ("[]", []),
            ('[{"id": 1}]', [{"id": 1}]),
            ('[{"id": 1}, {"id": 2}]', [{"id": 1}, {"id": 2}]),
        ],
    )
    def test_read_json_file_parametrized(
        self, tmp_path: Path, content: str, expected: List[Dict[str, Any]]
    ) -> None:
        """Параметризованный тест для разных содержимых файлов."""
        file_path = tmp_path / "param.json"
        file_path.write_text(content, encoding="utf-8")

        result = read_json_file(str(file_path))
        assert result == expected
