## Модуль generators

### filter_by_currency
Фильтрует транзакции по валюте.

```python
usd_transactions = filter_by_currency(transactions, "USD")
for transaction in usd_transactions:
    print(transaction)