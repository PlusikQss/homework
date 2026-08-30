### `src/decorators.py`

#### `log(filename: Optional[str] = None) -> Callable`
Декоратор для логирования работы функции.

**Параметры:**
- `filename` — имя файла для записи логов. Если не указан, логи выводятся в консоль.

**Пример использования:**

```python
from src.decorators import log

@log()
def my_function(x, y):
    return x + y

my_function(1, 2)
# Вывод в консоль: my_function ok

@log(filename="mylog.txt")
def my_function_with_file(x, y):
    return x + y

my_function_with_file(3, 4)
# В файл mylog.txt запишется: my_function_with_file ok