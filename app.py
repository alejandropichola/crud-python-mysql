import controllers.update as update
import controllers.insert as insert
import controllers.delete as delete
import controllers.select as select


# insert.insertUser("maiver1@gmail.com", "maiver", "pichola", "f", "")

class App:
    def __init__(self):
        self.dato = 1

    def menu(self):
        selection = 1
        while selection != 0:
            print("---------------------------------")
            print("               Menu              ")
            print("---------------------------------")
            print("1) Listar usuarios")
            print("2) Insertar usuario")
            print("3) Modificar usuario")
            print("4) Eliminar usuario")
            print("0) Salir")
            selection = input("Ingresa opción: ")
            if selection == '1':
                select.selectUser()
            elif selection == '2':
                insert.insertUser()
            elif selection == '3':
                update.updateUser()
            elif selection == '4':
                delete.deleteUser()
            elif selection == '0':
                selection = 0
            else:
                print("Opción invalida")


app = App()
app.menu()
