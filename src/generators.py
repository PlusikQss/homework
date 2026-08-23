from typing import Any, Dict, Iterator, List, Generator


def filter_by_currency(
    transactions: List[Dict[str, Any]], currency_code: str
) -> Iterator[Dict[str, Any]]:
    """
    Фильтрует транзакции по валюте.

    Параметры
    ---------
    transactions : List[Dict[str, Any]]
        Список транзакций.
    currency_code : str
        Код валюты для фильтрации (например, "USD").

    Возвращает
    ----------
    Iterator[Dict[str, Any]]
        Итератор с транзакциями в указанной валюте.
    """
    for transaction in transactions:
        operation_amount = transaction.get("operationAmount", {})
        currency = operation_amount.get("currency", {})
        if currency.get("code") == currency_code:
            yield transaction


def transaction_descriptions(transactions: List[Dict[str, Any]]) -> Generator[str, None, None]:
    """
    Возвращает описания транзакций по очереди.

    Параметры
    ---------
    transactions : List[Dict[str, Any]]
        Список транзакций.

    Возвращает
    ----------
    Generator[str, None, None]
        Генератор, выдающий описание каждой операции.
    """
    for transaction in transactions:
        yield transaction.get("description", "")


def card_number_generator(start: int, stop: int) -> Generator[str, None, None]:
    """
    Генерирует номера банковских карт в формате XXXX XXXX XXXX XXXX.

    Параметры
    ---------
    start : int
        Начальное значение диапазона.
    stop : int
        Конечное значение диапазона.

    Возвращает
    ----------
    Generator[str, None, None]
        Генератор, выдающий номера карт в заданном диапазоне.
    """
    for number in range(start, stop + 1):
        # Форматируем номер в 16-значное число с ведущими нулями
        card_number = f"{number:016d}"
        # Разбиваем на блоки по 4 цифры
        formatted_number = " ".join(
            card_number[i : i + 4] for i in range(0, 16, 4)
        )
        yield formatted_number
