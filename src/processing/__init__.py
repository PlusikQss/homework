from typing import Any, Dict, List


def filter_by_state(
    operations: List[Dict[str, Any]],
    state: str = "EXECUTED"
) -> List[Dict[str, Any]]:
    """
    Фильтрует список операций по статусу.

    Args:
        operations: Список словарей с данными об операциях.
        state: Статус для фильтрации. По умолчанию — 'EXECUTED'.

    Returns:
        Список операций, у которых ключ 'state' равен переданному значению.
    """
    return [op for op in operations if op.get("state") == state]


def sort_by_date(
    operations: List[Dict[str, Any]],
    reverse: bool = True
) -> List[Dict[str, Any]]:
    """
    Сортирует список операций по дате.

    Args:
        operations: Список словарей с данными об операциях.
        reverse: Порядок сортировки. По умолчанию True (от новых к старым).

    Returns:
        Отсортированный список операций.
    """
    # Даты в ISO-формате можно сортировать лексикографически
    return sorted(
        operations,
        key=lambda x: x.get("date", ""),
        reverse=reverse
    )
