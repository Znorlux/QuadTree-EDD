from Program import *
from QuadTree import *

if __name__ == "__main__":
    print("ARCHIVE MANAGER")
    print("------------------------------------------")
    print()
    Raiz = input("Nombre de su carpeta principal: ")
    print("------------------------------------------")
    print()
    tree = Folder(Raiz)#Folder hereda de QuadTree
    tree.pretty_print_tree(tree.root)# Imprimir en arbol
    program = Program(tree)#Arbol del programa
    program.show_menu()