# Створіть клас черги для роботи із символьними значеннями. Ви маєте створити реалізації для операцій над
# елементами:
# ■ IsEmpty — перевірка, чи черга пуста;
# ■ IsFull — перевірка черги на заповнення;
# ■ Enqueue — додати новий елемент до черги;
# ■ Dequeue — видалення елемента з черги;
# ■ Show — відображення на екрані всіх елементів черги.
# На старті додатка відобразіть меню, в якому користувач може вибрати необхідну операцію.

class Queue:
    def __init__(self, size) -> None:
        self.queue = []
        self.size = size
    def isEmpty(self):
        return len(self.queue) == 0
    
    def isFull(self):
        return len(self.queue) == self.size
    
    def enqueue(self, elem):
        if len(self.queue) < self.size:
            self.queue.append(elem)
        else:
            print("queue is full")
    
    def dequeue(self):
        if not self.isEmpty():
            item = self.queue.pop(0)
            return item
        else:
            print("queue is empty")
    
    def show(self):
        if not self.isEmpty():
            for el in self.queue:
                print(el)
        else:
            print("queue is empty")

queue = Queue(5)

queue.enqueue('wer')
queue.enqueue('poi')
queue.show()
print(queue.isEmpty())
print(queue.isFull())
queue.enqueue('fer')
queue.show()
print(queue.queue)
queue.dequeue()
queue.show()