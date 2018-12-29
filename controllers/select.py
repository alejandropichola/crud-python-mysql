import mysql.connector as MySQLdb
db = MySQLdb.connect(host="localhost", user="root", passwd="", db="api_python")


def selectUser():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users")
    result = cursor.fetchall()
    for x in result:
      id = x[0]
      email = x[3]
      firstName = x[1]
      lastName = x[2]
      gender = x[4]
      print("id: " + str(id))
      print("email: " + email)
      print("nombres: " + firstName)
      print("apellidos: " + lastName)
      print("Genero: " + gender)
      print(x)