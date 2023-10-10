import enum
import json
from pathlib import Path


class Categories(enum.Enum):
    Essentials ='Essentials'
    Entertainment = 'Entertainment'
    Charity = 'Charity'


def get_datasource() -> Path:
    # TODO: Exercise: what could go wrong ?
    return Path.cwd() / 'data' / 'budget.json'


def read(path: Path) -> dict:
    # TODO: Exercise: what could go wrong ?
    with open(path) as db:
        return json.load(db)


def write(path: Path, data: dict) -> bool:
    with open(path, 'w') as db:
        json.dump(data, db, indent=4)
    return True


def get_max_id(data):
    # TODO: Exercise: what could go wrong ?
    return max(int(record_id) for record_id in data)


def insert(path: Path, record: dict) -> bool:
    data = read(path)
    new_id = get_max_id(data) + 1
    data[new_id] = record
    return write(path, data)


def get_average_value(category, data):
    # Filter records by category
    records_in_category = [int(record['amount']) for record in data.values() if record['category'] == category.value]

    # TODO: Exercise: what could go wrong ?
    average = sum(records_in_category) / len(records_in_category)

    return average
