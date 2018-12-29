import mysql.connector as MySQLdb
import moment
import validators

db = MySQLdb.connect(host="localhost", user="root", passwd="", db="api_python")


def updateUser():
    try:
        id = int(input("Ingrese id: "))
    except ValueError:
        print("Ingrese un dato entero mayor a 0")
    email = input("Ingrese correo: ")
    firstName = input("Ingrese nombres: ")
    lastName = input("Ingrese apellidos: ")
    gender = input("ingrese genero M o F: ")
    birthDate = input("Ingrese fecha de nacimiento formato DD-MM-YYYY: ")
    if id <= 0:
        print('el id es necesario')
        return ''
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
        sql = "UPDATE users SET last_name='" + lastName + "', first_name='" + firstName + "', email='" + email + "', gender='" + gender + "', birth_date='" + inputDate + "' WHERE id=" + str(id)
        cursor = db.cursor()
        cursor.execute(sql)
    except ValueError as error:
        print(error)