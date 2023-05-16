from Program import *
from QuadTree import *

class Program:
    def __init__(self, tree):
        self.tree = tree
        self.folder_stack = [tree.root.value]  # Pila de carpetas visitadas, inicializada con la carpeta raíz

    def show_menu(self):
        print("""
MENU
Tienes las siguientes opciones:
1) Añadir una carpeta
2) Añadir un archivo
3) Editar el nombre una carpeta
4) Modificar archivo de una carpeta
5) Entrar en una carpeta
6) Retroceder a la carpeta anterior
7) Salir
    """)
        self.get_menu_answer()

    def get_menu_answer(self):
        answer = input("Opción: ")
        # Añadir una carpeta
        if answer == "1":
            self.add_folder()

        # Añadir un archivo
        elif answer == "2":
            self.add_file()

        # Editar nombre de una carpeta
        elif answer == "3":
            self.edit_folder_name()

        elif answer == "4":
            self.edit_file()

        elif answer == "5":
            self.access_folder()

        elif answer == "6":
            self.go_back()

        elif answer == "7":
            print("Chao")
            return

        self.show_menu()

    def add_folder(self):
        root = self.tree.root.value  # Carpeta raíz
        current_folder = input("Ingrese el nombre de la carpeta en la que quiere añadir elementos: ")
        folder = root.find_node_by_name(current_folder)

        if folder is None:
            print("La carpeta no existe\n")
        elif isinstance(folder, File):
            print(f"{folder.name} no es una carpeta, es un archivo, no puede añadir nada sobre un archivo\n")
        else:
            if folder.is_full():
                print("La carpeta actual está llena\n")
            else:
                folder_name = input("Ingrese el nombre de la nueva carpeta: ")
                if root.duplicate_name(folder_name):  # Verificamos que no exista una carpeta con ese mismo nombre
                    print("El nombre ya existe, vuelve a intentarlo con otro\n")
                else:
                    folder.add_folder(folder_name)
                    folder.pretty_print_tree(folder.root)
                    print()

    def add_file(self):
        root = self.tree.root.value  # Carpeta raíz
        current_folder = input("Ingrese el nombre de la carpeta en la que quiere añadir elementos: ")
        folder = root.find_node_by_name(current_folder)
        if folder is None:
            print("La carpeta no existe\n")
        elif isinstance(folder, File):
            print(f"{folder.name} no es una carpeta, es un archivo, no puede añadir nada sobre un archivo\n")
        else:
            if folder.is_full():
                print("La carpeta actual está llena\n")
            else:
                file_name = input("Ingrese el nombre del archivo que desea añadir: ")
                if folder.duplicate_name(file_name):
                    print("El nombre de archivo ya existe, vuelve a intentarlo con otro\n")
                else:
                    file_extension = input("Ingrese la extensión de su archivo (.txt / .pdf, etc...): ")
                    file_size = input("Ingrese el tamaño de su archivo: ")
                    folder.add_file(file_name, file_extension, file_size)
                    folder.pretty_print_tree(folder.root)
                    print()

    def edit_folder_name(self):
        root = self.tree.root.value
        current_folder = input("Ingrese el nombre de la carpeta a la que desea cambiarle el nombre: ")
        folder = root.find_node_by_name(current_folder)
        if folder is None:
            print("La carpeta no existe\n")
        elif isinstance(folder, File):
            print(f"{folder.name} no es una carpeta, es un archivo, si desea modificarlo, utilice su opción correspondiente\n")
        elif folder.name == "raiz":
            print("No puedes cambiarle el nombre a la carpeta raíz, vuelve a intentarlo con otro")
        else:
            new_folder_name = input(f"Ingrese el nuevo nombre para la carpeta {folder.name}: ")
            if root.duplicate_name(new_folder_name):  # Verificamos que no exista una carpeta con ese mismo nombre (OJO, debe preguntarse desde la raíz)
                print("El nombre de esa carpeta ya existe, vuelve a intentarlo con otro\n")
            else:
                folder.name = new_folder_name
                print("El nombre de la carpeta ha cambiado correctamente!")
                folder.pretty_print_tree(folder.root)

    def edit_file(self):
        root = self.tree.root.value
        current_file = input("Ingrese el nombre del archivo que desea modificar: ")
        file = root.find_node_by_name(current_file)
        if file is None:
            print("El archivo no existe\n")
        elif isinstance(file, Folder):
            print(f"{file.name} no es un archivo, es una carpeta, vuelve a intentarlo")
        else:
            while True:
                edit = input("\n¿Qué desea modificar del archivo? (nombre, extensión, peso): ").lower()
                if edit == "nombre":
                    new_file_name = input("Ingrese el nuevo nombre del archivo: ")
                    if root.duplicate_name(new_file_name):
                        print("El nombre de archivo ya existe, vuelve a intentarlo con otro")
                    else:
                        file.name = new_file_name
                        print("El nombre del archivo ha sido cambiado correctamente!")
                        root.pretty_print_tree(root.root)
                        break
                elif edit == "extensión":
                    new_ext = input("Ingrese la nueva extensión del archivo: ")
                    file.extension = new_ext
                    print("La extensión del archivo ha sido cambiada correctamente!")
                    break
                elif edit == "peso":
                    new_size = input("Ingrese el nuevo peso del archivo: ")
                    file.size = new_size
                    print("El peso del archivo ha sido cambiado correctamente!")
                    break
                else:
                    print("Ingrese un atributo del archivo válido, vuelva a intentarlo")

    def access_folder(self):
        folder_name = input("Ingrese el nombre de la carpeta a la que desea entrar: ")
        folder = self.tree.root.value.find_node_by_name(folder_name)

        if folder is None:
            print("La carpeta no existe\n")
        elif isinstance(folder, File):
            print("No es una carpeta, es un archivo\n")
        else:
            self.folder_stack.append(folder)  # Agregar la carpeta a la pila de carpetas visitadas
            print("------------------------------------------")
            print()
            folder.pretty_print_tree(folder.root)
            print()

    def go_back(self):
        if len(self.folder_stack) > 1:  # Verificar si hay al menos 2 elementos en la pila
            self.folder_stack.pop()  # Eliminar la carpeta actual de la pila
            previous_folder = self.folder_stack[-1]  # Obtener la carpeta anterior en la pila
            print("------------------------------------------")
            print()
            previous_folder.pretty_print_tree(previous_folder.root)
            print()  
        else:
            print("No hay carpetas anteriores a las que regresar\n")

