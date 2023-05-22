import psycopg2 as ps
import config


def exec_query(query: str) -> list:
    with ps.connect(dbname=config.db_name, user=config.user) as conn:
        with conn.cursor() as cur:
            cur.execute(query)
            res = cur.fetchall()
    return res
