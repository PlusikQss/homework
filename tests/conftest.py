from typing import Any, Dict, List

import pytest


@pytest.fixture
def sample_operations() -> List[Dict[str, Any]]:
    """Набор операций для тестов processing."""
    return [
        {"id": 1, "state": "EXECUTED", "date": "2024-06-01T12:00:00"},
        {"id": 2, "state": "CANCELED", "date": "2024-05-20T09:30:00"},
        {"id": 3, "state": "EXECUTED", "date": "2024-07-10T18:45:00"},
        {"id": 4, "state": "CANCELED", "date": "2024-04-01T08:00:00"},
        {"id": 5, "state": "EXECUTED", "date": "2024-06-15T10:00:00"},
    ]


@pytest.fixture
def transactions() -> List[Dict[str, Any]]:
    """Тестовые транзакции для generators."""
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {"name": "USD", "code": "USD"},
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {"name": "USD", "code": "USD"},
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {"name": "руб.", "code": "RUB"},
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
    ]
