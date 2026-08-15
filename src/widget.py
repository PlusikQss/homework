from datetime import datetime
from typing import Any, Dict, Optional

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(operation: Dict[str, Any]) -> Optional[str]:
    """
    Маскирует номер карты или счёта в зависимости от типа операции.
    operation: словарь вида {"type": "card" | "account", "number": "..."}
    Возвращает замаскированную строку или None, если тип неизвестен.
    """
    op_type = operation.get("type")
    number = operation.get("number", "")

    if not isinstance(number, str):
        number = str(number)

    if op_type == "card":
        return get_mask_card_number(number)
    elif op_type == "account":
        return get_mask_account(number)
    else:
        return None


def get_date(date_input: Optional[str]) -> Optional[str]:
    """
    Парсит дату из разных форматов и возвращает в формате YYYY-MM-DD.
    Поддерживает: YYYY-MM-DD, DD.MM.YYYY, YYYY/MM/DD.
    Для пустой строки или невалидной даты возвращает None.
    """
    if not date_input or not isinstance(date_input, str):
        return None

    date_input = date_input.strip()
    if date_input == "":
        return None

    # Пробуем ISO формат YYYY-MM-DD
    try:
        dt = datetime.fromisoformat(date_input)
        return dt.strftime("%Y-%m-%d")
    except ValueError:
        pass

    # Формат DD.MM.YYYY
    try:
        dt = datetime.strptime(date_input, "%d.%m.%Y")
        return dt.strftime("%Y-%m-%d")
    except ValueError:
        pass

    # Формат YYYY/MM/DD
    try:
        dt = datetime.strptime(date_input, "%Y/%m/%d")
        return dt.strftime("%Y-%m-%d")
    except ValueError:
        pass

    return None
