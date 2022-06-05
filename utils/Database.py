import mysql.connector
import json


class Database:
    def __del__(self):
        self._conn.close()

    def connect(self, db_host, db_user, db_pass, db_name):
        self._conn = mysql.connector.connect(host=db_host,
                                             database=db_name,
                                             user=db_user,
                                             password=db_pass)

    def insert_jobs(self, strategy, version, jobs):
        cursor = self._conn.cursor()

        query = "INSERT INTO jobs\
            (status, asset, year, timeframe, strategy, version, params)\
            VALUES ('idle', %s, %s, %s, %s, %s, %s)"

        for job in jobs:
            cursor.execute(query, (
                job['asset'],
                job['year'],
                job['timeframe'],
                strategy,
                version,
                job['params']
            ))

        self._conn.commit()
