import json
import os
import re
from typing import Dict, List

from src.logger import logger_setup

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path_log = os.path.join(current_dir, "../logs", "services.log")
logger = logger_setup("services", file_path_log)


def search_transaction_by_mobile_phone(transactions: List[Dict]) -> str:
    """Функция возвращает транзакции в описании которых есть мобильный номер"""
    try:
        mobile_pattern = re.compile(r"\+\d{1,4}")
        found_transactions = []
        for transaction in transactions:
            description = transaction.get("Описание", "")
            if mobile_pattern.search(description):
                found_transactions.append(transaction)
        logger.info("Выполнен поиск по транзакциям с номером телефона")
        return json.dumps(found_transactions, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"Возникла ошибка {e}")
        logger.error(f"Возникла ошибка {e}")
        return ""
