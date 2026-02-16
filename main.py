class Book:
    def __init__(self, title, author, status):
        self._title = title
        self._author = author
        self._status = status
    
class Person:
    def __init__(self, name):
        self._name = name

class Librarian(Person):
    def __init__(self, name):
        super().__init__(name)
        self._books = []
        self._visitors = []

    def addBook(self, title, author, status):
        self._books.append(Book(title, author, status))
        print("Книга добавлена!")

    def delete(self, title):
        for book in self._books:
            if book._title == title:
                self._books.remove(book)
                print("Книга успешно удалена")
                return
            
        print("Книга не найдена")

    def addUser(self):
        name = input("Имя пользователя: ")
        visitor = Visitor(name)
        self._visitors.append(visitor)
        print("Пользователь зарегистрирован")

    def showUsers(self):
        print("Все пользователи")
        found = False
        for visitor in self._visitors:
            print(visitor._name)
            found = True
        if not found:
            print("Нет пользователей")

    def showBooks(self):
        print("Все книги")
        if not self._books:
            print("Нет книг")

        else:
            for book in self._books:
                print(book._title + " " + book._author + " " + book._status)

class Visitor(Person):
    def __init__(self, name):
        super().__init__(name)
        self._books = []

    def showBooks(self, allBooks):
        print("Доступные книги")
        available = False

        for book in allBooks:
            if book._status == "Есть":
                print(book._title + " " + book._author)
                available = True

        if not available:
            print("Нет доступных книг")

    def takeBook(self, allBooks):
        title = input("Название книги: ")
        for book in allBooks:
            if book._title == title:
                if book._status == "Есть":
                    book._status = "Нет"
                    self._books.append(book)
                    print("Книга взята")

                else:
                    print("Книга уже выдана")

                return
        print("Книга не найдена")

print("Библиотека")
print("Библиотекарь (1)")
print("Пользователь (2)")

librarian = None

while True:
    choice = int(input("Выберите роль: "))

    if choice == 1:
        name = input("Ваше имя: ")
        librarian = Librarian(name)
        
        while True:
            print("Добавить книгу (1)")
            print("Удалить книгу (2)")
            print("Зарегистрировать пользователя (3)")
            print("Показать всех пользователей (4)")
            print("Показать все книги (5)")
            print("Выйти (0)")
            
            choice = int(input("Выберите: "))
            
            if choice == 1:
                title = input("Название: ")
                author = input("Автор: ")
                status = input("Доступна ли: ")
                librarian.addBook(title, author, status)

            elif choice == 2:
                title = input("Название: ")
                librarian.delete(title)

            elif choice == 3:
                librarian.addUser()

            elif choice == 4:
                librarian.showUsers()

            elif choice == 5:
                librarian.showBooks()

            elif choice == 0:
                break

    elif choice == 2:
        name = input("Ваше имя: ")

        if librarian is None:
            print("Сперва зайдите за библиотекаря")
            continue
        
        for visitor in librarian._visitors:
            if visitor._name == name:
                visitor = visitor
            
            archiveLib = Librarian("Библиотека")
            archiveLib.addBook("Книга №1", "Автор №1", "Есть")
            archiveLib.addBook("Книга №2", "Автор №2", "Есть")
            
            while True:
                print("Пользователь: " + visitor._name)
                print("Посмотреть книги (1)")
                print("Взять книгу (2)")
                print("Выйти (0)")
                
                action = int(input("Выберите: "))
                
                if action == 1:
                    visitor.showBooks(archiveLib._books)

                elif action == 2:
                    visitor.takeBook(archiveLib._books)

                elif action == 0:
                    break
        
        else:
            print("Создайте пользователя!")
            break