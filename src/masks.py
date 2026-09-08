import logging
from pathlib import Path

# Создаём логер для модуля masks
logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)

# Создаём папку logs, если её нет
log_dir = Path(__file__).parent.parent / "logs"
log_dir.mkdir(exist_ok=True)

# Настраиваем file_handler
file_handler = logging.FileHandler(log_dir / "masks.log", mode="w", encoding="utf-8")
file_handler.setLevel(logging.DEBUG)

# Настраиваем форматер
file_formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
file_handler.setFormatter(file_formatter)

# Добавляем handler к логеру
logger.addHandler(file_handler)


def get_mask_card_number(number: str) -> str:
    """Маскирует номер карты в формат XXXX XX** **** XXXX."""
    logger.debug(f"Вызов функции get_mask_card_number с аргументом: {number}")

    if not number:
        logger.error("Номер карты не может быть пустым.")
        raise ValueError("Номер карты не может быть пустым.")

    if not number.isdigit():
        logger.error(f"Номер карты должен содержать только цифры: {number}")
        raise ValueError("Номер карты должен содержать только цифры.")

    if len(number) < 4:
        logger.error(f"Длина номера карты должна быть не менее 4 цифр: {number}")
        raise ValueError("Длина номера карты должна быть не менее 4 цифр.")

    if len(number) != 16:
        result = "****"
        logger.debug(f"Возвращаем: {result}")
        return result

    result = f"{number[:4]} {number[4:6]}** **** {number[-4:]}"
    logger.debug(f"Успешное выполнение. Возвращаем: {result}")
    return result


def get_mask_account(number: str) -> str:
    """Маскирует номер счёта в формат **XXXX."""
    logger.debug(f"Вызов функции get_mask_account с аргументом: {number}")

    if not number:
        logger.error("Номер счёта не может быть пустым.")
        raise ValueError("Номер счёта не может быть пустым.")

    if not number.isdigit():
        logger.error(f"Номер счёта должен содержать только цифры: {number}")
        raise ValueError("Номер счёта должен содержать только цифры.")

    if len(number) < 4:
        logger.error(f"Номер счёта должен содержать не менее 4 цифр: {number}")
        raise ValueError("Номер счёта должен содержать не менее 4 цифр.")

    result = f"**{number[-4:]}"
    logger.debug(f"Успешное выполнение. Возвращаем: {result}")
    return result
