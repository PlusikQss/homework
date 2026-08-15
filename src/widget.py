from datetime import datetime
from typing import Optional

from .masks import get_mask_account, get_mask_card_number


def mask_account_card(info: str) -> str:
    """
    Принимает строку вида:
      "Visa Platinum 7000792289606361" или
      "Счет 73654108430135874305"

    Определяет тип по первым словам и применяет соответствующую маску.
    Возвращает строку с уже замаскированным номером.
    """
    parts = info.strip().split()
    if len(parts) < 2:
        raise ValueError("Некорректный формат строки: ожидается 'Тип Номер'.")

    number = parts[-1]
    prefix = " ".join(parts[:-1])

    # Простая эвристика: если в префиксе есть слово "Счет"
    # (регистронезависимо) — это счёт
    if "счет" in prefix.lower():
        masked_number = get_mask_account(number)
    else:
        # Иначе считаем, что это карта
        masked_number = get_mask_card_number(number)

    return f"{prefix} {masked_number}"


def get_date(date_input: Optional[str]) -> str:
    if not date_input:
        return ""

    dt = datetime.fromisoformat(date_input)
    return dt.strftime("%d.%m.%Y")
