class Item:
    def __init__(self, valor):
        self.valor = valor
        self.next = None
    
class Lista:
    def __init__(self):
        self.head = None
        self.next = None
        self.size = 0
    
    def isEmpty(self):
        return self.size == 0
    
    def mostrar(self):
        atual = self.head
        while atual is not None:
            print(atual.valor, end=' ')
            atual = atual.next
        print('')
        
    def inserir_final(self, valor):
        novoItem = Item(valor)
        
        if self.head is None:
            self.head = novoItem
        else:
            atual = self.head
            while atual.next is not None:
                atual = atual.next
            atual.next = novoItem
        self.size += 1
        
    def inserir_inicio(self, valor):
        novoItem = Item(valor)
        novoItem.next = self.head
        self.head = novoItem
        self.size += 1
        
    def remover_inicio(self):
        if self.head is None:
            print('Lista vazia.')
        else:
            self.head = self.head.next
            self.size -= 1
            
    def remover_final(self):
        if self.head is None:
            print('Lista vazia.')
        
        if self.head.next is None:
            valorRemovido = self.head.valor
            self.head = None
            return valorRemovido

        atual = self.head
        while atual.next.next is not None:
            atual = atual.next

        valorRemovido = atual.next.valor
        atual.next = None
        return valorRemovido
        