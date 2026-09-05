import os
from typing import Any, Dict

import requests
from dotenv import load_dotenv

# Загружаем переменные окружения
load_dotenv()


def convert_to_rub(transaction: Dict[str, Any]) -> float:
    """
    Конвертирует сумму транзакции в рубли.

    Параметры
    ---------
    transaction : Dict[str, Any]
        Словарь с данными о транзакции.

    Возвращает
    ----------
    float
        Сумма транзакции в рублях.
    """
    operation_amount = transaction.get("operationAmount", {})
    amount = float(operation_amount.get("amount", 0))
    currency_code = operation_amount.get("currency", {}).get("code", "")

    # Если валюта уже рубли — возвращаем сумму
    if currency_code == "RUB":
        return amount

    # Для USD и EUR обращаемся к API
    if currency_code in ("USD", "EUR"):
        api_key = os.getenv("API_KEY")
        api_url = os.getenv("API_URL", "https://api.apilayer.com/exchangerates_data")

        if not api_key:
            raise ValueError("API_KEY не найден в .env")

        url = f"{api_url}/convert?to=RUB&from={currency_code}&amount={amount}"

        headers = {"apikey": api_key}
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        result = response.json()
        return float(result["result"])

    # Для других валют возвращаем сумму как есть
    return amount
