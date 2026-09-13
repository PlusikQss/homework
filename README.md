### `src/csv_excel_reader.py`

#### `read_csv_file(file_path: str) -> List[Dict[str, Any]]`
Читает CSV-файл с финансовыми операциями и возвращает список словарей.

```python
from src.csv_excel_reader import read_csv_file

transactions = read_csv_file("data/transactions.csv")
print(transactions)