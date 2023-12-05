# Розробіть додаток, який дозволяє зберігати інформацію
# про логіни і паролі користувачів. Кожному користувачеві
# відповідає пара «логін — пароль». При старті додатку
# відображається меню:
# ■ Додати нового користувача;
# ■ Видалити існуючого користувача;
# ■ Перевірити, чи існує такий користувач;
# ■ Змінити логін існуючого користувача;
# ■ Змінити пароль існуючого користувача.
# Для реалізації завдання обов’язково застосуйте одну
# із структур даних. При виборі структури керуйтеся постановкою завдання. 

class Node:
    def __init__(self, data: tuple, prev=None, next=None) -> None:
        self.data = data
        self.prev = prev
        self.next = next

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        new_node.prev = last_node
    
    def remove(self, data_to_rm):
        current = self.head
        prev = None

        while current:
            if current.data == data_to_rm:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next

                if current.next:
                    current.next.prev = current.prev
                
                return True
            current = current.next

        return False
    
    def show_list(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    def contains(self, value):
        current = self.head
        while current:
            if current.data.get_login() == value:
                return True
            current = current.next
        return False
    
    def replace(self, old_value, new_value):
        current = self.head
        while current:
            if current.data == old_value:
                current.data = new_value
                return True
            current = current.next
        return False

class User:
    def __init__(self, login, password) -> None:
        self.__login = login
        self.__password = password
    
    def get_login(self):
        return self.__login
    def set_login(self, new_login):
        self.__login = new_login

    def get_password(self):
        return self.__password
    def set_password(self, new_password):
        self.__password = new_password

    def __str__(self) -> str:
        return f"[{self.__login}, {self.__password}]"

class UserList(User):
    def __init__(self) -> None:
        self.user_list = DoublyLinkedList()

    def addUser(self, user: User):
        if not self.user_list.contains(user.get_login()):
            self.user_list.append(user)
        else:
            print("Login already taken")
    
    def remove_user(self, user):
        if self.user_list.contains(user.get_login()):
            self.user_list.remove(user)
            print(f"user {user.get_login()} removed")
        else:
            print("User not found")
    
    def exists(self, login):
       return self.user_list.contains(login)

    def show(self):
        self.user_list.show_list()

    def replace_login(self, old_login, new_login):
        current = self.user_list.head
        while current:
            if current.data.get_login() == old_login:
                current.data.set_login(new_login)
                print(f"Login for user {old_login} replaced, new login: {new_login}")
                return
            current = current.next
        print(f"User '{old_login}' not found")


    def replace_password(self, login, new_password):
        current = self.user_list.head
        while current:
            if current.data.get_login() == login:
                current.data.set_password(new_password)
                print(f"Password for user '{login}' replaced")
                return
            current = current.next
        print(f"User '{login}' not found")



ul = UserList()
        
user1 = User('lw', '1234')
user2 = User('lq', '124145')
user3 = User('lw', "1234")
user4 = User('io', 'asd')
user5 = User('sd', "12465")

ul.addUser(user1)
ul.addUser(user2)
ul.addUser(user3)
ul.addUser(user4)
ul.show()
ul.remove_user(user2)
ul.remove_user(user5)
ul.show()
print(ul.exists("io"))


ul.replace_password('lw', 'qwerty')
ul.replace_login('lw', 'lu')
ul.show()