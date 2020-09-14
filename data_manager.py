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
    query = """
        SELECT first_name, last_name, city
        FROM mentor
        WHERE city = %(mentor_city)s
        ORDER BY first_name"""
    args = {'mentor_city': mentor_city}
    cursor.execute(query, args)
    return cursor.fetchall()



@database_common.connection_handler
def get_all_applicans(cursor: RealDictCursor) -> list:
    query ="""
        SELECT first_name, last_name, phone_number, application_code
        FROM applicant
        ORDER BY first_name"""
    cursor.execute(query)
    return cursor.fetchall()

@database_common.connection_handler
def get_applicant_data_by_name(cursor: RealDictCursor, applicant_name: str) -> list:
    query ="""
        SELECT first_name, last_name, phone_number FROM applicant
        WHERE first_name = %(applicant_name)s OR last_name = %(applicant_name)s
        ORDER BY first_name"""
    args = {'applicant_name': applicant_name}
    cursor.execute(query, args)
    return cursor.fetchall()


# @database_common.connection_handler
# def get_applicant_data_by_email(cursor: RealDictCursor, applicants_email: str) -> list:
#     query = """
#             SELECT * FROM applicant
#             WHERE email LIKE %(applicants_email)s
#             ORDER BY first_name"""
#     args = {'applicants_email': applicants_email}
#     cursor.execute(query, args)
#     return cursor.fetchall()

@database_common.connection_handler
def get_applicants_data_by_email(cursor: RealDictCursor, applicans_email: str) -> list:
    cursor.execute("""
        SELECT first_name, last_name, phone_number
        FROM applicant
        WHERE email LIKE (%s)
        ORDER BY first_name""", ["%"+applicans_email])
    return cursor.fetchall()


# SELECT first_name, last_name, phone_number FROM applicant
#             WHERE email LIKE %(applicants_email)s
#             ORDER BY first_name"""

@database_common.connection_handler
def get_applicant_info(cursor: RealDictCursor, application_code: str) -> list:
    query = """
                        SELECT * FROM applicant
                        WHERE application_code = %(application_code)s
                        ORDER BY first_name
                       """
    args={'application_code': application_code}
    cursor.execute(query, args)

    return cursor.fetchall()

@database_common.connection_handler
def update_nr(cursor: RealDictCursor, new_nr: str, application_code: str) -> list:
    query = """
                            UPDATE applicant
                            SET phone_number= %(new_nr)s
                            WHERE application_code = %(application_code)s
                           """
    args = {'application_code': application_code, 'new_nr': new_nr}
    cursor.execute(query, args)

    return None


@database_common.connection_handler
def delete(cursor: RealDictCursor, application_code: str) -> list:
    query = """
                            DELETE FROM applicant
                            WHERE application_code = %(application_code)s
                           """
    args = {'application_code': application_code}
    cursor.execute(query, args)

    return None


@database_common.connection_handler
def delete_by_email_ending(cursor: RealDictCursor, applicans_email: str) -> list:
        cursor.execute("""
            DELETE FROM applicant
            WHERE email LIKE (%s)
            """,
                       ["%" + applicans_email])
        return None


@database_common.connection_handler
def append_applicant(cursor: RealDictCursor, name: str,phone: int, last_name: str, email: str,code: int) -> list:
    query = """
                                INSERT INTO applicant (first_name, last_name, phone_number, email, application_code)
                                VALUES (%(name)s, %(last_name)s, %(phone)s ,%(email)s, %(code)s);
                               """
    args = {'name': name,
            'last_name' : last_name,
            'phone' : phone,
            'email': email,
            'code' : code

            }

    cursor.execute(query, args)