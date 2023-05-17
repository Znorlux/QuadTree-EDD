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
            return "📄" # Emoji para archivo
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