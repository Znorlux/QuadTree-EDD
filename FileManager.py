#HOLAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA

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
        print(linea + ("└── " if is_left else "┌── ") + str(node.value))

        #Hijo 2 (izquierdo)
        if node.child2:
            self.pretty_print_tree(node.child2, linea + ("    " if is_left else "│   "), True)

        #Hijo 1 (izquierdo)
        if node.child1:
            self.pretty_print_tree(node.child1, linea + ("    " if is_left else "│   "), True)
        
    def find_node_by_name(self, name, node=None):
        if node is None:
            node = self.root
        if node is None:
            return None
        
        if isinstance(node.value, Folder) and node.value.name == name: #caso base
            current_folder = node.value
            print("Estas en la carpeta con nombre:",current_folder.name)
            print("")
            current_folder.pretty_print_tree(current_folder.root)           
            
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
    
    def add_file(self,name, extension, size):
        file = File(name,extension,size)
        self.add_node(file)

    def add_folder(self,name):
        folder = Folder(name)
        self.add_node(folder)

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
    
tree = QuadTree()
tree.add_node(0)
tree.add_node(1)
tree.add_node(2)
tree.add_node(3)
tree.add_node(4)

tree.add_folder("carpeta")
tree.add_file("file1",".txt","43")
tree.pretty_print_tree(tree.root)
tree.find_node_by_name("carpeta")

