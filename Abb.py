class Vertice:
    def __init__(self, key, payload):
        self.key = int(key)
        self.payload = payload
        self.pai = None
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.key)+" "+str(self.payload)

class Tree:
    def __init__(self):
        self.raiz = None
        self.count = 0

    def TreeInsert(self, z):
        y = None
        x = self.raiz

        while(x != None):
            y = x
            if (z.key < x.key):
                x = x.left
            else:
                x = x.right

        z.pai = y
        if(y == None): 
            self.raiz = z
        elif(z.key < y.key): 
            y.left = z
        else:
            y.right = z

        self.count += 1

    def iteractive_tree_search(self, key):
        if(self.raiz == None):
            return None

        vertice = self.raiz
        while(vertice != None and vertice.key != int(key)):
            if(int(key) < vertice.key):
                vertice = vertice.left
            else:
                vertice = vertice.right

        return vertice

    def inorder_tree_walk(self, vertice=None):
        if(self.raiz == None): 
            return

        if(vertice == None): 
            vertice = self.raiz

        if(vertice.left != None): # Condição de parada. Vértice esquerdo == None
            self.inorder_tree_walk(vertice=vertice.left)

        print(vertice) ##ou coloca print(vertice.payload) pq o exercicio pede pra imprimir o payload

        if(vertice.right != None): # Condição de parada. Vértice direito == None
            self.inorder_tree_walk(vertice=vertice.right) 
                                                         
    def tree_minimum(self, vertice=None):
        if(self.raiz == None): # Para o caso de uma árvore vazia
            return None
        if(vertice == None): # Primeiro nível de chamadas recursivas
            vertice = self.raiz
        while(vertice.left != None):
            vertice = vertice.left
        return vertice

    def tree_sucessor(self, vertice):
        if(vertice.right != None): # Caso 1 - possui a subárvore direita
            return self.tree_minimum(vertice.right)
        y = vertice.pai # Caso 2 - Não possui a subárvore direita. Volta na árvore até achar o
        while(y != None and vertice == y.right):#primeiro vértice que é pai pela subárvore esquerda
            vertice = y                         
            y = vertice.pai 
        return y

    def tree_predecessor(self, vertice):
        if(vertice.left != None):
            return self.tree_maximum(vertice.left)

        y = vertice.pai
        while(y != None and vertice == y.left):
            vertice = y
            y = vertice.pai

        return y

    def tree_transplant(self, u, v):
        if(u.pai == None): 
            self.raiz = v 
        elif(u.pai.left == u): 
            u.pai.left = v 
        else: # u é o filho direito do pai dele
            u.pai.right = v 
        if(v != None):
            v.pai = u.pai 

    # Remove um vértice da árvore
    
    def tree_remove(self, z):
        if(z.left == None): 
            self.tree_transplant(z, z.right) 
        elif(z.right == None):
            self.tree_transplant(z, z.left) 
        else: 
            y = self.tree_minimum(z.right) 
            if(y.pai != z): 
                self.tree_transplant(y, y.right)
                y.right = z.right 
                y.right.pai = y
            self.tree_transplant(z, y) 
            y.left = z.left 
            y.left.pai = y

    def inorder_tree_walk_dec(self, vertice=None):
        if(vertice == None):
            vertice = self.raiz

        if(vertice.right != None):
            self.inorder_tree_walk_dec(vertice=vertice.right)

        print(vertice.payload) ##ou coloca print(vertice) pra deixar igual o pdf

        if(vertice.left != None):
            self.inorder_tree_walk_dec(vertice=vertice.left)

    def tree_maximum(self, vertice=None):
        if(self.raiz == None): # Para o caso de uma árvore vazia
            return None

        if(vertice == None): # Primeiro nível de chamadas recursivas
            vertice = self.raiz

        while(vertice.right != None):
            vertice = vertice.right

        return vertice
        
    def tree_minimum_rec(self, vertice=None):
        if(self.raiz == None):
            return None
        if(vertice == None):
            vertice = self.raiz
        if(vertice.left != None):
            return self.tree_minimum_rec(vertice.left)
        else:
            return vertice
        
## Menu do pdf, erro na tentativa de converter para tuple(...)
##def menu():
##    linha = input().split()
##    op = int(linha[0])
##    while(op >=0 and op <=10):
##        if(op in [0, 3, 4, 8, 9, 10]):
##            return tuple(op)
##        elif(op == 1):
##            return tuple(op, int(linha[1]), "".join(linha[2:]))
##        elif(op in [2, 5, 6, 7]):
##            return tuple(op, int(linha[1]))
##        else:
##            print("Opção inválida")
##
##        linha = input().split()
##        op = int(linha[0])
    
def menu():
    linha = input().split()
    op = int(linha[0])
    while(op >=0 and op <=10):
        if(op in [0, 3, 4, 8, 9, 10]):
            return [op]
        elif(op == 1):
            return [op, int(linha[1]), "".join(linha[2:])]
        elif(op in [2, 5, 6, 7]):
            return [op, int(linha[1])]
        else:
            print("Opção inválida")
        linha = input().split()
        op = int(linha[0])

tree = Tree()
op = menu()
while(op[0] != 0):
    if(op[0]==1):
        vertice=Vertice(op[1], op[2])
        tree.TreeInsert(vertice)
        
    elif(op[0]==2):
        vertice = tree.iteractive_tree_search(op[1])
        if(vertice != None):
            print(vertice.payload)
        else:
            print('INEXISTENTE')
            
    elif(op[0]==3):
        tree.inorder_tree_walk()
        
    elif(op[0]==4):
        vertice = tree.tree_minimum()
        if(vertice == None):
            print('INEXISTENTE')
        else:
            print(vertice.payload)
            
    elif(op[0]==5):
        vertice = tree.iteractive_tree_search(op[1])
        if vertice == None:
            print('INEXISTENTE')
        else:
            sucessor = tree.tree_sucessor(vertice)
            if (sucessor == None):
                print('INEXISTENTE')
            else:
                print(sucessor.payload)
                
    elif(op[0]==6):
        vertice = tree.iteractive_tree_search(op[1])
        if(vertice == None):
            print('INEXISTENTE')
        else:
            predecessor = tree.tree_predecessor(vertice)
            if (predecessor == None):
                print('INEXISTENTE')
            else:
                print(predecessor.payload)
                
    elif(op[0]==7):
        vertice = tree.iteractive_tree_search(op[1])
        if(vertice == None):
            print('INEXISTENTE')
        else:
            tree.tree_remove(vertice)
            print('REMOVIDO')
            
    elif(op[0]==8):
        vertice = tree.tree_minimum_rec()
        if(vertice == None):
            print('INEXISTENTE')
        else:
            print(vertice.payload)
            
    elif(op[0]==9):
        vertice = tree.tree_maximum()
        if(vertice == None):
            print('INEXISTENTE')
        else:
            print(vertice.payload)
            
    elif(op[0]==10):
        tree.inorder_tree_walk_dec()

    op = menu()
