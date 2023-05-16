class QuadNode:
    def __init__(self, value):# Value es objeto de tipo File o Folder
        self.value = value
        self.child1 = None
        self.child2 = None
        self.child3 = None
        self.child4 = None

    def is_folder(self):
        return isinstance(self.value, Folder)
    
    def is_file(self):
        return isinstance(self.value, File)
class QuadTree:
    def __init__(self):
        self.root = None

    def add_node(self, value, nodes=None):
        if nodes is None:
            nodes = [self.root] if self.root else []
        current = nodes.pop(0) if nodes else self.root
        if current is None:
            self.root = QuadNode(value)
            return
        else:
            if current.child1 is None:
                current.child1 = QuadNode(value)
                return
            else:
                nodes.append(current.child1)
            if current.child2 is None:
                current.child2 = QuadNode(value)
                return
            else:
                nodes.append(current.child2)
            if current.child3 is None:
                current.child3 = QuadNode(value)
                return
            else:
                nodes.append(current.child3)
            if current.child4 is None:
                current.child4 = QuadNode(value)
                return
            else:
                nodes.append(current.child4)
        if nodes is not None:
            self.add_node(value, nodes)

    def get_node_icon(self, node):
        if isinstance(node, Folder):
            return "📁"  # Emoji para carpeta
        elif isinstance(node, File):
            return "📄"  # Emoji para archivo
        else:
            return ""

    def pretty_print_tree(self, node, linea="", is_left=False):
        if self.root is None:
            print("Empty Tree")
            return
        #Hijo 4 (derecho)
        if node.child4:
            self.pretty_print_tree(node.child4, linea + ("│   " if is_left else "    "), False)

        #Hijo 3 (derecho)
        if node.child3:
            self.pretty_print_tree(node.child3, linea + ("│   " if is_left else "    "), False)

        #Carpeta principal
        print(linea + ("└── " if is_left else "┌── ") + str(node.value.name) + " " + self.get_node_icon(node.value))

        #Hijo 2 (izquierdo)
        if node.child2:
            self.pretty_print_tree(node.child2, linea + ("    " if is_left else "│   "), True)

        #Hijo 1 (izquierdo)
        if node.child1:
            self.pretty_print_tree(node.child1, linea + ("    " if is_left else "│   "), True)
        
    def find_node_by_name(self, name, node=None):
        if node is None:
            node = self.root

        if isinstance(node.value, Folder) and node.value.name == name:
            return node.value
        
        if isinstance(node.value, File) and node.value.name == name:
            return node.value

        if node.child1:
            result = self.find_node_by_name(name, node.child1)
            if result:
                return result
            elif isinstance(node.child1.value, Folder):
                sub_result = self.find_node_by_name(name, node.child1.value.root)
                if sub_result:
                    return sub_result

        if node.child2:
            result = self.find_node_by_name(name, node.child2)
            if result:
                return result
            elif isinstance(node.child2.value, Folder):
                sub_result = self.find_node_by_name(name, node.child2.value.root)
                if sub_result:
                    return sub_result

        if node.child3:
            result = self.find_node_by_name(name, node.child3)
            if result:
                return result
            elif isinstance(node.child3.value, Folder):
                sub_result = self.find_node_by_name(name, node.child3.value.root)
                if sub_result:
                    return sub_result

        if node.child4:
            result = self.find_node_by_name(name, node.child4)
            if result:
                return result
            elif isinstance(node.child4.value, Folder):
                sub_result = self.find_node_by_name(name, node.child4.value.root)
                if sub_result:
                    return sub_result

        return None
    

class File:
    def __init__(self, name, extension, size):
        self.name = name
        self.extension = extension
        self.size = size
    
class Folder(QuadTree):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.root = QuadNode(self)
        self.amount = 0

    def add_file(self,name, extension, size):
        file = File(name,extension,size)
        self.root.value.add_node(file)
        self.amount += 1

    def add_folder(self,name):
        folder = Folder(name)
        self.root.value.add_node(folder)
        self.amount += 1

    def is_full(self):
        if(self.amount == 4):
            return True
        else:
            return False
        
    def duplicate_name(self, name):
        element = self.find_node_by_name(name)
        if element != None:
            return True
        else:
            return False
        
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


if __name__ == "__main__":
    print("ARCHIVE MANAGER")
    print("------------------------------------------")
    print()
    #Raiz = input("Nombre de su carpeta principal: ")
    Raiz = "raiz"
    print("------------------------------------------")
    print()
    tree = Folder(Raiz)#Folder hereda de QuadTree
    tree.add_folder("folder1")
    tree.add_file("file1","txt","42")
    #print(tree.root.child1.value.name)
    tree.root.child1.value.add_folder("folder999")

    #print(tree.root.child1.value.root.child1.value.name)
    #tree.root.child1.value.root.child1.value.add_folder("folder69")
    #print(tree.root.child1.value.root.child1.value.root.child1.value.name)
    #print(tree.root.child1.value.root.child1.value.name)
    #print(tree.find_node_by_name("folder1"))
    #print("PRUEBA AQUI: ", (tree.find_node_by_name("folder69").name)) #deberia traerme al objeto de Folder01
    #print(tree.root.child2)

    #tree.add_folder("folder2")
    #tree.add_file("file1","txt","42")
    tree.pretty_print_tree(tree.root)# Imprimir en arbol
    #tree.root.child1.value.pretty_print_tree(tree.root.child1.value.root)
    program = Program(tree)#Arbol del programa
    #Inicio del flujo
    program.show_menu()

