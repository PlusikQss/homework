import json
import logging
from pathlib import Path
from typing import Any, Dict, List

# Создаём логер для модуля utils
logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)

# Создаём папку logs, если её нет
log_dir = Path(__file__).parent.parent / "logs"
log_dir.mkdir(exist_ok=True)

# Настраиваем file_handler
file_handler = logging.FileHandler(log_dir / "utils.log", mode="w", encoding="utf-8")
file_handler.setLevel(logging.DEBUG)

# Настраиваем форматер
file_formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
file_handler.setFormatter(file_formatter)

# Добавляем handler к логеру
logger.addHandler(file_handler)


def read_json_file(file_path: str) -> List[Dict[str, Any]]:
    """
    Читает JSON-файл и возвращает список словарей.

    Параметры
    ---------
    file_path : str
        Путь к JSON-файлу.

    Возвращает
    ----------
    List[Dict[str, Any]]
        Список словарей с данными. Если файл пустой,
        содержит не-список или не найден — возвращает пустой список.
    """
    logger.debug(f"Вызов функции read_json_file с аргументом: {file_path}")

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        if isinstance(data, list):
            logger.debug(f"Файл {file_path} успешно прочитан. Количество записей: {len(data)}")
            return data

        logger.error(f"Файл {file_path} содержит не-список.")
        return []

    except FileNotFoundError:
        logger.error(f"Файл {file_path} не найден.")
        return []
    except json.JSONDecodeError:
        logger.error(f"Файл {file_path} содержит некорректный JSON.")
        return []
