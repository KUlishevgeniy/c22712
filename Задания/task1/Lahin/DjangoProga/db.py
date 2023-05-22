import psycopg2

def getcont2():
    connection = psycopg2.connect(host='localhost', dbname='dbdata', user='postgres', password='Q1w2e3r4')
    cursor = connection.cursor()
    cursor.execute("SELECT product, price, diagonal, resolution, cpu, ram, graphics_controller, volume, src FROM laptops")
    fetched = cursor.fetchall()
    return fetched
    cursor.close()
    connection.close()
print(getcont2())