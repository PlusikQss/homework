from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(data: str) -> str:
    """
    Принимает строку формата:
    - "Visa Platinum 7000792289606361"
    - "Счет 73654108430135874305"
    Возвращает строку с замаскированным номером.
    """
    if not data or not isinstance(data, str):
        raise ValueError("Входные данные должны быть непустой строкой.")

    parts = data.split()
    if len(parts) < 2:
        raise ValueError("Некорректный формат: ожидается тип и номер.")

    # Ищем номер — это последний элемент, который содержит только цифры
    number = parts[-1]
    name = " ".join(parts[:-1])

    if not number.isdigit():
        raise ValueError("Номер должен содержать только цифры.")

    # Определяем тип по первому слову
    if parts[0].lower() == "счет":
        masked = get_mask_account(number)
    else:
        masked = get_mask_card_number(number)

    return f"{name} {masked}"


def get_date(date_string: str) -> str:
    """
    Принимает строку с датой в формате ISO (например, "2024-03-11T02:26:18.671407").
    Возвращает дату в формате "ДД.ММ.ГГГГ".
    """
    if not date_string or not isinstance(date_string, str):
        raise ValueError("Входные данные должны быть непустой строкой.")

    # Разбираем только дату (часть до T)
    date_part = date_string.split("T")[0]

    try:
        # Пробуем ISO формат
        dt = datetime.fromisoformat(date_part)
        return dt.strftime("%d.%m.%Y")
    except ValueError as exc:
        raise ValueError("Некорректный формат даты.") from exc
