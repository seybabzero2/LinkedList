import random
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    def getData(self):
        return self.data
    def getNext(self):
        return self.next
    def setNext(self, next):
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def add_at_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        if self.tail is None:
            self.tail = new_node
    def add_at_tail(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        n = self.tail
        n.next = new_node
        self.tail = new_node
    def view_list(self):
        if self.head is None:
            print('Лист порожній')
            return
        else:
            n = self.head
            while n is not None:
                print(n.data, " ", end='')
                n = n.next
            print()
    def delete_at_head(self):
        if self.tail is None:
            print('Лист порожній')
            return
        else:
            n = self.head
            self.head = n.next
    def delete_at_tail(self):
        if self.tail is None:
            print('Лист порожній')
            return
        else:
            n = self.head
            while n.next.next is not None:
                self.tail = n.next
                n = n.next
            n = self.tail
            n.next = None
    def create_random_list(self, n):        # Створення списку з випадковими значеннями
        for i in range(0, n, 1):
            pipi.add_at_head(random.randint(0, 10))
    
    def len_all_node(self):                 # Підраховує кількість вузлів у списку
        s = 0
        n = self.head
        while n is not None:
            s += 1
            n = n.next
        return s

    def delete_Node(self, data):            # Видаляє вузол за значенням data
        n = self.head
        while n.data is not data:
            n = n.next
        if n.next is None:
            n = self.tail
        else:
            n.data = n.next.data
            n.next = n.next.next

    def clear(self, data):                   # Очищення списку
        n = self.head
        for i in range(self.len_all_node()): # Старт цикла для очищення
            if n.next is None:              
                n = self.tail
            else:
                n.data = n.next.data         # Очищення
                n.next = n.next.next         # Очищення

    def finding_one(self):                   # Створює тимчасову список для вбудову біля одиниці нуля
        n = self.head   
        temp = []                            # Ініціалізація тимчасової списку
        for i in range(self.len_all_node()): # Старт цикла для пошуку одиниць
            if (n.data == 1):                # Перевірка, чи ця нода має значення 1
                temp.append(n.data)
                temp.append(0)
            else:
                temp.append(n.data)  
            n = n.next                       # Перехід до іншої ноди
        self.add_zero_at_one(temp)           # Посилання на функцію з параметром data

    def add_zero_at_one(self, temp):
        temp.reverse()                       # Перевертаємо список для заповнення його через голову
        n = self.head
        self.clear(n.data)                   # Очищення списку
        for i in range(len(temp)):           # Старт цикла для заповнення данних у пустий массив з списку temp
            self.add_at_head(temp[i])       
        self.delete_at_tail()                # Видаляє копію останнього елемента

pipi = LinkedList()
n = int(input('Вкажіть розмір зв\'язного списку '))
pipi.create_random_list(n)
print("Початковий список: \t", end = '')
pipi.view_list()
pipi.finding_one()
print("Вихідний список: \t", end = '')
pipi.view_list()
pipi.delete_Node(int(input('\nЧисло яке хочете видалити з списку')))
print("Вихідний список: \t", end = '')
pipi.view_list()


