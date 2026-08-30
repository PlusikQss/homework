from functools import wraps
from typing import Any, Callable, Optional, TypeVar, cast

# Тип для декоратора
F = TypeVar("F", bound=Callable[..., Any])


def log(filename: Optional[str] = None) -> Callable[[F], F]:
    """
    Декоратор для логирования работы функции.

    Параметры
    ---------
    filename : Optional[str]
        Имя файла для записи логов. Если None — логи выводятся в консоль.

    Возвращает
    ----------
    Callable[[F], F]
        Декорированная функция.
    """

    def decorator(func: F) -> F:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                log_message = f"{func.__name__} ok"
            except Exception as exc:
                log_message = (
                    f"{func.__name__} error: {type(exc).__name__}. "
                    f"Inputs: {args}, {kwargs}"
                )

                # Логируем сообщение
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(log_message + "\n")
                else:
                    print(log_message)

                # Пробрасываем оригинальное исключение
                raise exc

            # Логируем успешное выполнение
            if filename:
                with open(filename, "a", encoding="utf-8") as file:
                    file.write(log_message + "\n")
            else:
                print(log_message)

            return result

        return cast(F, wrapper)

    return decorator
