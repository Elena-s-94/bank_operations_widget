from datetime import datetime
from typing import List, Dict


def filter_by_state(
    data_list: List[Dict],
    state: str = "EXECUTED",
) -> List[Dict]:
    """Фильтрует список словарей по состоянию.

    Параметры:
        data_list (List[Dict]): Список словарей с данными о транзакциях.
        state (str): Состояние для фильтрации (по умолчанию 'EXECUTED').

    Возвращает:
        List[Dict]: Новый список словарей с указанным состоянием.
    """
    return [item for item in data_list if item.get("state") == state]


from datetime import datetime
from typing import List, Dict

def filter_by_state(
    data_list: List[Dict],
    state: str = "EXECUTED",
) -> List[Dict]:
    """Фильтрует список словарей по состоянию."""
    return [item for item in data_list if item.get("state") == state]

def sort_by_date(
    data_list: List[Dict],
    descending: bool = True,
) -> List[Dict]:
    """Сортирует список словарей по дате."""
    
    def parse_date(item: Dict) -> datetime | None:
        date_str = item.get("date")
        if not date_str:
            return None
        try:
            return datetime.fromisoformat(date_str.strip())
        except ValueError:
            return None

    return sorted(
        data_list,
        key=lambda x: parse_date(x),
        reverse=descending,
    )
   """ Параметры:
        data_list (List[Dict]): Список словарей с данными о транзакциях.
        descending (bool): Порядок сортировки. По умолчанию — True (по убыванию).

    Возвращает:
        List[Dict]: Отсортированный список словарей.
    """
    def parse_date(item: Dict) -> datetime | None:
        date_str = item.get("date")
        if not date_str:
            return None
       
        try:
            return datetime.fromisoformat(date_str.strip())
        except ValueError:
 
    return sorted(
        data_list,
        key=lambda x: parse_date(x),
        reverse=descending,
    )
