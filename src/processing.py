from datetime import datetime
from typing import Any, Dict, List


def filter_by_state(
    operations: List[Dict[str, Any]], state: str = "EXECUTED"
) -> List[Dict[str, Any]]:
    """
    Фильтрует список операций по значению ключа 'state'.

    Параметры
    ---------
    operations : List[Dict[str, Any]]
        Список словарей с данными о банковских операциях.
    state : str, optional
        Значение ключа 'state' для фильтрации (по умолчанию 'EXECUTED').

    Возвращает
    ----------
    List[Dict[str, Any]]
        Новый список, содержащий только операции с указанным state.
    """
    return [op for op in operations if op.get("state") == state]


def sort_by_date(
    operations: List[Dict[str, Any]], reverse: bool = True
) -> List[Dict[str, Any]]:
    """
    Сортирует список операций по дате.

    Параметры
    ---------
    operations : List[Dict[str, Any]]
        Список словарей с данными о банковских операциях.
    reverse : bool, optional
        Порядок сортировки: True — по убыванию (сначала новые), False — по возрастанию.
        По умолчанию True.

    Возвращает
    ----------
    List[Dict[str, Any]]
        Новый отсортированный список операций.
    """

    def parse_date(op: Dict[str, Any]) -> datetime:
        date_str = op.get("date", "")
        return datetime.fromisoformat(date_str)

    return sorted(operations, key=parse_date, reverse=reverse)
