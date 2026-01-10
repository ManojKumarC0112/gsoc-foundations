#task 1
# class Student():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def intoduce(self):
#         return f"{self.name} is {self.age} years old"
#     def birthday(self):
#         self.age=1+self.age
# student1=Student("manoj",20)
# student1.birthday()
# print(student1.intoduce())
# stundent2=Student("pari",14)
# print(stundent2.intoduce())


#task 2
class BankAccount():
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance
    def deposit(self,amount):
        self.balance=self.balance+amount
        return f"your curent balance is ${self.balance}"
    def withdraw(self,amount):
        if amount>self.balance:
            return f"You don't have enough money"
        else:
            self.balance=self.balance-amount
            return f"You have withdrawn.{amount}"
bank1=BankAccount("John",100)
print(bank1.deposit(100))
print(bank1.withdraw(90))
print(bank1.withdraw(1000))