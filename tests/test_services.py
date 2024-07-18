import json

from src.services import search_transaction_by_mobile_phone


def test_search_transaction_by_mobile_phone() -> None:
    transactions = [
        {"Описание": "Я МТС +7 921 11-22-33", "Сумма операции": -1000},
        {"Описание": "Тинькофф Мобайл +7 995 555-55-55", "Сумма операции": -1500},
        {"Описание": "Магазин", "Сумма операции": -500},
        {"Описание": "МТС Mobile +7 981 333-44-55", "Сумма операции": -2000},
        {"Описание": "Оплата по карте", "Сумма операции": -300},
    ]

    expected_output = json.dumps(
        [
            {"Описание": "Я МТС +7 921 11-22-33", "Сумма операции": -1000},
            {"Описание": "Тинькофф Мобайл +7 995 555-55-55", "Сумма операции": -1500},
            {"Описание": "МТС Mobile +7 981 333-44-55", "Сумма операции": -2000},
        ],
        ensure_ascii=False,
        indent=4,
    )

    result = search_transaction_by_mobile_phone(transactions)
    assert result == expected_output
