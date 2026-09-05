### `src/utils.py`

#### `read_json_file(file_path: str) -> List[Dict[str, Any]]`
Читает JSON-файл и возвращает список словарей. Если файл пустой, содержит не-список или не найден — возвращает пустой список.

```python
from src.utils import read_json_file

transactions = read_json_file("data/operations.json")
print(transactions)