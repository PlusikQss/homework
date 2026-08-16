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
