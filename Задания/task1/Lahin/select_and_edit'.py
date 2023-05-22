
import psycopg2
import config
def edit(request):
    try:
        connection = psycopg2.connect(host=config.host, dbname=config.dbname, user=config.user, password=config.password)
        cursor = connection.cursor()
        cursor.execute(request)
        print("Done")
    except Exception as error:
        print(f"Что-то не так. Ошибка:{error}")
    finally:
        cursor.close()
        connection.close()
def select(request):
    try:
        connection = psycopg2.connect(host=config.host, dbname=config.dbname, user=config.user,
                                      password=config.password)
        cursor = connection.cursor()
        cursor.execute(request)
        result = cursor.fetchall()
    except Exception as error:
         result = f"Ошибка: {error}"
    finally:
        cursor.close()
        connection.close()
        return result