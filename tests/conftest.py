from typing import Any, Dict, List

import pytest


@pytest.fixture
def sample_operations() -> List[Dict[str, Any]]:
    return [
        {
            "id": 1,
            "state": "EXECUTED",
            "date": "2024-06-01T12:00:00",
            "description": "Перевод",
            "amount": 1000,
        },
        {
            "id": 2,
            "state": "CANCELED",
            "date": "2024-05-20T09:30:00",
            "description": "Оплата",
            "amount": 500,
        },
        {
            "id": 3,
            "state": "EXECUTED",
            "date": "2024-07-10T18:45:00",
            "description": "Снятие",
            "amount": 200,
        },
    ]
