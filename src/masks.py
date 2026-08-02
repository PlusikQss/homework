def get_mask_card_number(card_number: str) -> str:
    """
    Маскирует номер карты: видны первые 6 и последние 4 цифры.
    Формат: XXXX XX** **** XXXX
    """
    if len(card_number) != 16 or not card_number.isdigit():
        raise ValueError("Card number must be a 16-digit string.")

    first_four = card_number[:4]
    next_two = card_number[4:6]
    last_four = card_number[-4:]

    return f"{first_four} {next_two}** **** {last_four}"


def get_mask_account(account_number: str) -> str:
    """
    Маскирует номер счёта: видны только последние 4 символа.
    Формат: **XXXX (для строк длиной ≥ 4).
    """
    if len(account_number) < 4:
        raise ValueError("Account number must be at least 4 characters long.")

    last_four = account_number[-4:]
    # Количество звёздочек = вся длина минус 4 видимые цифры
    stars = "*" * (len(account_number) - 4)

    return f"{stars}{last_four}"