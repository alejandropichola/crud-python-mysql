import mysql.connector as MySQLdb
import moment
import validators

db = MySQLdb.connect(host="localhost", user="root", passwd="", db="api_python")


def insertUser():
    email = input("Ingrese correo: ")
    firstName = input("Ingrese nombres: ")
    lastName = input("Ingrese apellidos: ")
    gender = input("ingrese genero M o F: ")
    birthDate = input("Ingrese fecha de nacimiento formato DD-MM-YYYY: ")
    inputDate = ''
    if validators.email(email) != True:
        print('Ingresa un email valido')
        return ''
    gender = gender.upper()

    if (gender != 'M' and gender != 'F'):
        print('ingrese un genero valido')
    if len(firstName) <= 0:
        print('nombre requerido')
        return ''
    try:
        if len(birthDate) > 0:
            inputDate = moment.date(birthDate, 'DD-MM-YYYY').format('YYYY-MM-DD')
        else:
            inputDate = moment.now().format('YYYY-MM-DD')
    except ValueError:
        inputDate = moment.now().format('YYYY-MM-DD')
    try:
        sql = "INSERT INTO users values (null, '" + lastName + "', '" + firstName + "', '" + email + "', '" + gender + "', '" + inputDate + "')"
        print(sql)
        #cursor = db.cursor()
        #cursor.execute(sql)
    except ValueError as error:
        print(error)
