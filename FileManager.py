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
            #print("Estas en la carpeta con nombre:",current_folder.name)
            #print("")
            #file = File("test",".xml","42")
            #file2 = File("test2",".xml","41")
            #current_folder.add_element(file)
            #current_folder.add_element(file2)
            #current_folder.pretty_print_tree(current_folder.root)
            return current_folder           
            
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

    def duplicate_name(self, name):
        element = self.find_node_by_name(name)
        if element != None:
            return True
        else:
            return False

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
4. Modificar archivo una carpeta""")
        self.get_menu_answer()

    def get_menu_answer(self):
        root = tree.root.value #Carpeta raiz
        answer = input("Opcion: ")
        if answer == "1":
            current_folder = input("Ingrese el nombre de la carpeta en la que quiere añadir elementos: ")
            folder = root.find_node_by_name(current_folder)
            if folder == None:
                print("La carpeta no existe\n")
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
        self.show_menu()
    


tree = Folder("Raiz")#Folder hereda de QuadTree
tree.pretty_print_tree(tree.root)
tree.add_folder("test")
tree.add_folder("test2")
tree.add_folder("test3")
#tree.add_folder("Raiz")#Carpeta raiz

program = Program(tree)
#Inicio del flujo
program.show_menu()

#tree.find_node_by_name("carpeta")

