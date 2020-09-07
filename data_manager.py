from typing import List, Dict

from psycopg2 import sql
from psycopg2.extras import RealDictCursor

import database_common


@database_common.connection_handler
def get_mentors(cursor: RealDictCursor) -> list:
    query = """
        SELECT first_name, last_name, city
        FROM mentor
        ORDER BY first_name"""
    cursor.execute(query)
    return cursor.fetchall()


@database_common.connection_handler
def get_mentors_by_last_name(cursor: RealDictCursor, last_name: str) -> list:
    query ="""
        SELECT first_name, last_name, city
        FROM mentor
        WHERE last_name = %(last_name)s
        ORDER BY first_name"""
    args = {'last_name': last_name}
    cursor.execute(query, args)
    return cursor.fetchall()

@database_common.connection_handler
def get_mentors_by_city(cursor: RealDictCursor, mentor_city: str) -> list:
    query ="""
        SELECT first_name, last_name, city
        FROM mentor
        WHERE city = %(mentor_city)s
        ORDER BY first_name"""
    args = {'mentor_city': mentor_city}
    cursor.execute(query, args)
    return cursor.fetchall()


