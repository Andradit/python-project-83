import psycopg2
from psycopg2.extras import DictCursor


def create_connection(database_url):
    return psycopg2.connect(database_url)


def close_connection(conn):
    conn.close()


def get_urls(conn):
    with conn.cursor() as curr:
        query = ("""
                SELECT
                urls.id,
                urls.name,
                MAX(url_checks.created_at),
                url_checks.status_code
                FROM urls
                LEFT JOIN url_checks ON urls.id = url_checks.url_id
                GROUP BY urls.id, urls.name, url_checks.status_code
                ORDER BY urls.id DESC
                """)
        curr.execute(query)
        urls = curr.fetchall()
    return urls


def add_url(conn, name):
    with conn.cursor() as curr:
        curr.execute("""
             INSERT INTO urls (name)
             VALUES (%s)
             RETURNING id""", (name,))
        url_id = curr.fetchone()[0]
    conn.commit()
    return url_id


def get_current_url(conn, url_id):
    with conn.cursor() as curr:
        curr.execute("SELECT * FROM urls WHERE id = %s", (url_id,))
        url = curr.fetchone()
    return url


def get_url_by_name(conn, name):
    with conn.cursor() as curr:
        curr.execute("SELECT * FROM urls WHERE name = %s", (name,))
        url = curr.fetchone()
        return url


def add_url_check(conn, url_id, status_code, h1, title, description):
    with conn.cursor() as curr:
        curr.execute("""
        INSERT INTO url_checks (url_id, status_code, h1, title, description)
        VALUES (%s, %s, %s, %s, %s)""",
                     (url_id, status_code, h1, title, description))
    conn.commit()
    return


def get_url_checks(conn, url_id):
    with conn.cursor() as curr:
        curr.execute("""
                    SELECT *
                    FROM url_checks
                    WHERE url_id = %s
                    ORDER BY created_at DESC
                    """, (url_id,))
        url_checks = curr.fetchall()
    return url_checks

