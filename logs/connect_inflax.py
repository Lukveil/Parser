from influxdb import InfluxDBClient

import sqlite3

influx_client = InfluxDBClient(host='localhost', port=8086, database='peewee_log_10')
inf_dat = list()

conn = sqlite3.connect('log_db.db')
cursor = conn.cursor()
cursor.execute('select * from user')
list_res = cursor.fetchall()
for result in list_res:

    data = {
        'measurement': 'user_activity',  # Имя метрики
        'tags': {
            'id': result[0],
            'team': result[4],
            'project': result[5],
            'version': result[6],
            'operate': result[7],
        },
        'fields': {
            'user': result[3],
            'operate': result[7],
        },
        'time': result[2]
    }
    inf_dat.append(data)

influx_client.write_points(inf_dat)
