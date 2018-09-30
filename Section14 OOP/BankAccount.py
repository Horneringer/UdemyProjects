class Account:
    def __init__(self, filepath):  # конструктор объекта
        self.filepath = filepath  # теперь мы можем использовать переменную filepath в любом методе класса,
        # не создавая новую
        with open(filepath, 'r') as file:
            self.balance = float(file.read())  # баланс в качестве начального атрибута объекта; приводим к типу int
    
    def withdraw(self, amount):  # метод снятия средств
        self.balance = self.balance - amount
    
    def deposit(self, amount):  # метод внесения средств
        self.balance = self.balance + amount
    
    def commit(self):  # метод, который сохраняет изменение баланса, записывая новое значение в файл
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))


class Checking(Account):  # для наследования в параметрах дочернего класса указывается класс-родитель
    """This class generates checking account object"""  # многострочный комментарий внутри класса,
    #  может использоваться для его описания
    
    def __init__(self, filepath, fee):
        Account.__init__(self, filepath)  # когда вызывается конструктор класса
        # Checking(дочерний), он в свою очередь вызывает конструктор класса Account(родительский), в этом случае
        # дочерний класс получает всю информацию о текущем счёте(если короче, просто наследуем метод __init__,
        # чтобы не множить код); переменная fee(комиссия) является уже собственностью класса Checking и дополнительно
        #  определяется через self
        self.fee = fee
    
    def transfer(self, amount):
        self.balance = self.balance - amount - (amount * self.fee / 100)  # перевод суммы с вычетом указанного
        # процента от этой суммы


checking = Checking('balance.txt', 10)  # объект класса Checking
print(checking.__doc__)  # метод позволяет вывести все многострочные комментарии(документацию), написанные в
# соответствующем классе, если их нет, будет None


# checking.deposit(300) # теперь методы родительского класса доступны и для класса-наследника
# checking.transfer(500)
# checking.commit()
# checking.withdraw(300)
# print(checking.balance, '$')

# account = Account('balance.txt')  # создаём объект класса и передаём путь к файлу
# print(account.balance)  # отображаем текущий баланс, указав через точку соответствующий атрибут
# account.withdraw(200)
# account.deposit(2200)
# account.commit()
# print(account.balance, '$')
