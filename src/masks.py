def get_mask_card_number(number: str) -> str:
    """Маскирует номер карты в формат XXXX XX** **** XXXX."""
    if not number:
        raise ValueError("Номер карты не может быть пустым.")

    if not number.isdigit():
        raise ValueError("Номер карты должен содержать только цифры.")

    if len(number) < 4:
        raise ValueError("Длина номера карты должна быть не менее 4 цифр.")

    if len(number) != 16:
        return "****"

    return f"{number[:4]} {number[4:6]}** **** {number[-4:]}"


def get_mask_account(number: str) -> str:
    """Маскирует номер счёта в формат **XXXX."""
    if not number:
        raise ValueError("Номер счёта не может быть пустым.")

    if not number.isdigit():
        raise ValueError("Номер счёта должен содержать только цифры.")

    if len(number) < 4:
        raise ValueError("Номер счёта должен содержать не менее 4 цифр.")

    return f"**{number[-4:]}"
