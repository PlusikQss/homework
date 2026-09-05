import json
from typing import Any, Dict, List


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
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        if isinstance(data, list):
            return data
        return []

    except (FileNotFoundError, json.JSONDecodeError):
        return []
