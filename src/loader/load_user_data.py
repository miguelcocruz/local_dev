from typing import Dict, List

import utils

users = [
    {'id': 1, 'name': 'miguel', 'price': 120000},
    {'id': 2, 'name': 'goncalo', 'price': 80000},
]


def insert_user_data(users: List[Dict]) -> None:
    insert_query = """
        INSERT INTO housing.user (id, name, price)
        VALUES (%(id)s, %(name)s, %(price)s)
    """
    with utils.connect() as conn:
        with conn.cursor() as cursor:
            cursor.executemany(insert_query, vars_list=users)


if __name__ == '__main__':
    insert_user_data(users)
