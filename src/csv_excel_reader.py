import logging
from pathlib import Path
from typing import Any, Dict, List

import pandas as pd

# Создаём логер для модуля
logger = logging.getLogger("csv_excel_reader")
logger.setLevel(logging.DEBUG)

# Создаём папку logs, если её нет
log_dir = Path(__file__).parent.parent / "logs"
log_dir.mkdir(exist_ok=True)

# Настраиваем file_handler
file_handler = logging.FileHandler(
    log_dir / "csv_excel_reader.log", mode="w", encoding="utf-8"
)
file_handler.setLevel(logging.DEBUG)

# Настраиваем форматер
file_formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
file_handler.setFormatter(file_formatter)

# Добавляем handler к логеру
logger.addHandler(file_handler)


def read_csv_file(file_path: str) -> List[Dict[str, Any]]:
    """
    Читает CSV-файл с финансовыми операциями.

    Параметры
    ---------
    file_path : str
        Путь к CSV-файлу.

    Возвращает
    ----------
    List[Dict[str, Any]]
        Список словарей с транзакциями.
        Если файл не найден или пустой — возвращает пустой список.
    """
    logger.debug(f"Вызов функции read_csv_file с аргументом: {file_path}")

    try:
        df = pd.read_csv(file_path)
        transactions = df.to_dict(orient="records")
        logger.debug(
            f"Файл {file_path} успешно прочитан. Количество записей: {len(transactions)}"
        )
        return transactions
    except FileNotFoundError:
        logger.error(f"Файл {file_path} не найден.")
        return []
    except Exception as exc:
        logger.error(f"Ошибка при чтении CSV-файла {file_path}: {exc}")
        return []


def read_excel_file(file_path: str) -> List[Dict[str, Any]]:
    """
    Читает Excel-файл с финансовыми операциями.

    Параметры
    ---------
    file_path : str
        Путь к Excel-файлу.

    Возвращает
    ----------
    List[Dict[str, Any]]
        Список словарей с транзакциями.
        Если файл не найден или пустой — возвращает пустой список.
    """
    logger.debug(f"Вызов функции read_excel_file с аргументом: {file_path}")

    try:
        df = pd.read_excel(file_path)
        transactions = df.to_dict(orient="records")
        logger.debug(
            f"Файл {file_path} успешно прочитан. Количество записей: {len(transactions)}"
        )
        return transactions
    except FileNotFoundError:
        logger.error(f"Файл {file_path} не найден.")
        return []
    except Exception as exc:
        logger.error(f"Ошибка при чтении Excel-файла {file_path}: {exc}")
        return []
