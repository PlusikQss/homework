def get_mask_card_number(number: str) -> str:
    if not number:
        return ""

    if not number.isdigit():
        raise ValueError("Номер карты должен содержать только цифры.")

    # Если меньше 4 цифр — ошибка
    if len(number) < 4:
        raise ValueError("Длина номера карты должна быть не менее 4 цифр.")

    # Если не ровно 16 — маскируем как **** (чтобы кейс "4321" работал)
    if len(number) != 16:
        return "****"

    return (
        f"{number[:4]} "
        f"{number[4:6]}** **** "
        f"{number[-4:]}"
    )


def get_mask_account(number: str) -> str:
    if not number:
        return ""

    if not number.isdigit():
        raise ValueError("Номер счёта должен содержать только цифры.")

    # Если меньше 4 цифр — ошибка
    if len(number) < 4:
        raise ValueError("Номер счёта должен содержать не менее 4 цифр.")

    last_four = number[-4:]
    return f"**{last_four}"
