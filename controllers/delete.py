import mysql.connector as MySQLdb

db = MySQLdb.connect(host="localhost", user="root", passwd="", db="api_python")


def deleteUser():
    try:
        id = int(input("Ingrese id: "))
    except ValueError:
        print("Ingrese un dato entero mayor a 0")

    if id > 0:
        print('id necesaria')

    try:
        sql = "DELETE FROM users WHERE id=" + id
        cursor = db.cursor()
        cursor.execute(sql)
    except ValueError as error:
        print(error)
