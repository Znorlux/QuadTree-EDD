<<<<<<< HEAD

=======
>>>>>>> 83185cb5758c9b292f7f99699f64c9bcd2cec92d
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

    def pretty_print_tree(self, node, linea="", is_left=False, last_child=False):
        if self.root is None:
            print("Empty Tree")
            return

        # Hijo 4 (derecho)
        if node.child4:
            self.pretty_print_tree(node.child4, linea + ("│   " if is_left else "    "), False,
                                   last_child=(not node.child3 and not node.child2 and not node.child1))
        # Hijo 3 (derecho)
        if node.child3:
            self.pretty_print_tree(node.child3, linea + ("│   " if is_left else "    "), False,
                                   last_child=(not node.child2 and not node.child1))
        print(linea + ("└── " if is_left else "┌── ") + str(node.value))

        if last_child:
            line = "    "
        else:
            line = "│   "

        # Hijo 2 (izquierdo)
        if node.child2:
            self.pretty_print_tree(node.child2, linea + (line if is_left else "│   "), True,
                                   last_child=(not node.child1))
        # Hijo 1 (izquierdo)
        if node.child1:
            self.pretty_print_tree(node.child1, linea + (line if is_left else "│   "), True, last_child=True)
        
    def find_node_by_name(self, name, node=None):
        if node is None:
            node = self.root
        if node is None:
            return None
        
        if isinstance(node.value, Folder) and node.value.name == name: #caso base
            current_folder = node.value
            return current_folder 
                  
        if isinstance(node.value, File) and node.value.name == name:
            current_file = node.value
            return current_file
        
        if node.child1:
            result = self.find_node_by_name(name, node.child1)
            if result:
                return result
        if node.child2:
            result = self.find_node_by_name(name, node.child2)
            if result:
                return result
        if node.child3:
            result = self.find_node_by_name(name, node.child3)
            if result:
                return result
        if node.child4:
            result = self.find_node_by_name(name, node.child4)
            if result:
                return result
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
        self.add_node(file)
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
<<<<<<< HEAD
        
=======

>>>>>>> 83185cb5758c9b292f7f99699f64c9bcd2cec92d
    def duplicate_name(self, name):
        element = self.find_node_by_name(name)
        if element != None:
            return True
        else:
            return False
<<<<<<< HEAD
        
=======


>>>>>>> 83185cb5758c9b292f7f99699f64c9bcd2cec92d
class Program:
    def __init__(self,tree):
        self.tree = tree

    def show_menu(self):
        print("""
Bienvenido al gestor de carpetas con arbol cuaternario
Tienes las siguientes opciones:
1. Añadir una carpeta
2. Añadir un archivo
3. Editar el nombre una carpeta
<<<<<<< HEAD
4. Modificar archivo de una carpeta
    """)
        self.get_menu_answer()

    def get_menu_answer(self):
        answer = input()
        #Añadir una carpeta
=======
4. Modificar archivo una carpeta""")
        self.get_menu_answer()

    def get_menu_answer(self):
        root = tree.root.value #Carpeta raiz
        answer = input("Opcion: ")
>>>>>>> 83185cb5758c9b292f7f99699f64c9bcd2cec92d
        if answer == "1":
            self.add_folder()

        #Añadir un archivo
        elif answer == "2":
            self.add_file()

        #Editar nombre de una carpeta
        elif answer == "3":
            self.edit_folder_name()

        elif answer == "4":
            self.edit_file()
        self.show_menu()
    

    def add_folder(self):
            root = tree.root.value #Carpeta raiz
            current_folder = input("Ingrese el nombre de la carpeta en la que quiere añadir elementos: ")
            folder = root.find_node_by_name(current_folder)
            if folder == None:
                print("La carpeta no existe\n")
            elif isinstance(folder, File):
                print(f"{folder.name} no es una carpeta, es un archivo, no puede añadir nada sobre un archivo\n")
            else:    
                if folder.is_full() == True:
                    print("La carpeta actual está llena\n")
                else:
                    folder_name = input("Ingrese el nombre de la nueva carpeta: ")
                    if folder.duplicate_name(folder_name):#Verificamos que no exista una carpeta con ese mismo nombre
                        print("El nombre ya existe, vuelve a intentarlo con otro\n")
                    else:
                        folder.add_folder(folder_name)
                        folder.pretty_print_tree(folder.root)
                        print()
    def add_file(self):
            root = tree.root.value #Carpeta raiz
            current_folder = input("Ingrese el nombre de la carpeta en la que quiere añadir elementos: ")
            folder = root.find_node_by_name(current_folder)
            if folder == None:
                print("La carpeta no existe\n")
            elif isinstance(folder, File):
                print(f"{folder.name} no es una carpeta, es un archivo, no puede añadir nada sobre un archivo\n")
            else:
                if folder.is_full() == True:
                    print("La carpeta actual está llena\n")
                else:
                    file_name = input("Ingrese el nombre del archivo que desea añadir: ")
                    if (folder.duplicate_name(file_name)):
                        print("El nombre de archivo ya existe, vuelve a intentarlo con otro\n")
                    else:
                        file_extension = input("Ingrese la extension de su archivo (.txt / .pdf, etc...) ")
                        file_size = input("Ingrese el tamaño de su archivo: ")
                        folder.add_file(file_name, file_extension, file_size)
                        folder.pretty_print_tree(folder.root)
                        print()

    def edit_folder_name(self):
        root = tree.root.value
        current_folder = input("Ingrese el nombre de la carpeta a la que desea cambiarle el nombre: ")
        folder = root.find_node_by_name(current_folder)
        if folder == None:
                print("La carpeta no existe\n")
        elif isinstance(folder, File):
            print(f"{folder.name} no es una carpeta, es un archivo, si desea modificarlo, utilice su opción correspondiente\n")
        elif folder.name == "raiz":
            print("No puedes cambiarle el nombre a la carpeta raiz, vuelve a intentarlo con otro")
        else:
            new_folder_name = input(f"Ingrese el nuevo nombre para la carpeta {folder.name}: ")
            if folder.duplicate_name(new_folder_name):#Verificamos que no exista una carpeta con ese mismo nombre
                    print("El nombre de esa carpeta ya existe, vuelve a intentarlo con otro\n")
            else:
                folder.name = new_folder_name
                print("El nombre de la carpeta ha cambiado correctamente!")
                folder.pretty_print_tree(folder.root)

<<<<<<< HEAD
    def edit_file(self):
        root = tree.root.value
        current_folder = input("Ingrese el nombre de la carpeta donde está el archivo: ")
        folder = root.find_node_by_name(current_folder)
        if folder == None:
            print("La carpeta no existe\n")
        elif isinstance(folder, File):
            print(f"{file.name} no es un archivo, es una carpeta, vuelve a intentarlo")
           
        current_file = input("Ingrese el nombre del archivo que desea modificar: ")
        file = folder.find_node_by_name(current_file)
        if file == None:
            print("El archivo no existe\n")
        elif isinstance(file, Folder):
            print(f"{file.name} no es un archivo, es una carpeta, vuelve a intentarlo")

        else:
            new_file_name = input("Ingrese el nuevo nombre del archivo: ")
            if folder.duplicate_name(new_file_name):
                print("El nombre de archivo ya existe, vuelve a intentarlo con otro")
            else:
                file.name = new_file_name
                print("El nombre del archivo ha sido cambiado correctamente!")
                folder.pretty_print_tree(folder.root)
            
tree = Folder("raiz")#Folder hereda de QuadTree
=======
tree = Folder("Raiz")#Folder hereda de QuadTree
tree.pretty_print_tree(tree.root)
>>>>>>> 83185cb5758c9b292f7f99699f64c9bcd2cec92d
tree.add_folder("test")
tree.add_folder("test2")
tree.add_file("file1","txt","42")
#tree.add_folder("Raiz")#Carpeta raiz

program = Program(tree)
#Inicio del flujo
program.show_menu()

#tree.find_node_by_name("carpeta")

