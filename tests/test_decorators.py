from pathlib import Path
from typing import List

import pytest

from src.decorators import log


class TestLogDecorator:

    def test_log_to_console_success(self, capsys: pytest.CaptureFixture[str]) -> None:
        """Проверяет вывод в консоль при успешном выполнении."""

        @log()
        def add_numbers(a: int, b: int) -> int:
            return a + b

        result = add_numbers(1, 2)

        assert result == 3

        captured = capsys.readouterr()
        assert "add_numbers ok" in captured.out

    def test_log_to_console_error(self, capsys: pytest.CaptureFixture[str]) -> None:
        """Проверяет вывод в консоль при ошибке."""

        @log()
        def divide_numbers(a: int, b: int) -> float:
            return a / b

        with pytest.raises(ZeroDivisionError):
            divide_numbers(1, 0)

        captured = capsys.readouterr()
        assert "divide_numbers error" in captured.out
        assert "ZeroDivisionError" in captured.out
        assert "Inputs: (1, 0)" in captured.out

    def test_log_to_file_success(self, tmp_path: Path) -> None:
        """Проверяет запись в файл при успешном выполнении."""
        log_file = tmp_path / "test_log.txt"

        @log(filename=str(log_file))
        def multiply_numbers(a: int, b: int) -> int:
            return a * b

        result = multiply_numbers(3, 4)

        assert result == 12

        with open(log_file, "r", encoding="utf-8") as file:
            content = file.read().strip()
        assert "multiply_numbers ok" in content

    def test_log_to_file_error(self, tmp_path: Path) -> None:
        """Проверяет запись в файл при ошибке."""
        log_file = tmp_path / "test_log.txt"

        @log(filename=str(log_file))
        def divide_numbers(a: int, b: int) -> float:
            return a / b

        with pytest.raises(ZeroDivisionError):
            divide_numbers(10, 0)

        with open(log_file, "r", encoding="utf-8") as file:
            content = file.read().strip()
        assert "divide_numbers error" in content
        assert "ZeroDivisionError" in content
        assert "Inputs: (10, 0)" in content

    def test_log_to_file_appends(self, tmp_path: Path) -> None:
        """Проверяет, что лог дописывается в файл, а не перезаписывается."""
        log_file = tmp_path / "test_log.txt"

        @log(filename=str(log_file))
        def simple_function() -> str:
            return "hello"

        simple_function()
        simple_function()

        with open(log_file, "r", encoding="utf-8") as file:
            lines = file.readlines()

        assert len(lines) == 2
        assert "simple_function ok" in lines[0]
        assert "simple_function ok" in lines[1]

    def test_log_with_args_and_kwargs(self, capsys: pytest.CaptureFixture[str]) -> None:
        """Проверяет логирование с аргументами и именованными аргументами."""

        @log()
        def complex_function(a: int, b: int, operation: str = "add") -> int:
            if operation == "add":
                return a + b
            return a - b

        result = complex_function(5, 3, operation="add")

        assert result == 8

        captured = capsys.readouterr()
        assert "complex_function ok" in captured.out

    def test_log_preserves_function_metadata(self) -> None:
        """Проверяет, что декоратор сохраняет метаданные функции."""

        @log()
        def sample_function(x: int) -> int:
            """Документация sample_function."""
            return x * 2

        assert sample_function.__name__ == "sample_function"
        assert sample_function.__doc__ == "Документация sample_function."

    @pytest.mark.parametrize(
        "a, b, expected",
        [(1, 2, 3), (10, 20, 30), (-5, 5, 0)],
    )
    def test_log_parameterized(
        self, capsys: pytest.CaptureFixture[str], a: int, b: int, expected: int
    ) -> None:
        """Параметризованный тест для разных входных данных."""

        @log()
        def add(a: int, b: int) -> int:
            return a + b

        result = add(a, b)

        assert result == expected

        captured = capsys.readouterr()
        assert "add ok" in captured.out
