# class Animal:
#     def speak(self):
#         print("Animal speaks.")

# class Cat(Animal):
#     def meow(self):
#         print("Cat meows.")

# class Dog(Animal):
#     def bark(self):
#         print("Dog barks.")

# my_cat = Cat()
# my_dog = Dog()
# my_cat.speak()  # Inheriting from Animal
# my_cat.meow()
# my_dog.speak()  # Inheriting from Animal
# my_dog.bark()



# # Define a class called "BankAccount" to represent a bank account
# class BankAccount:
#     # Constructor method to initialize the account with an account number and balance
#     def __init__(self, account_number, balance):
#         self.account_number = account_number  # Initialize the account number attribute
#         self.balance = balance  # Initialize the balance attribute

#     # Method to deposit money into the account
#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount  # Add the deposited amount to the balance

#     # Method to withdraw money from the account
#     def withdraw(self, amount):
#         if 0 < amount <= self.balance:
#             self.balance -= amount  # Subtract the withdrawn amount from the balance

#     # Method to retrieve the current balance of the account
#     def get_balance(self):
#         return self.balance  # Return the current balance


# # Define a base class called "Animal"



# class Grandparent:
#     def greet(self):
#         print("Hello from Grandparent!")

# class Parent(Grandparent):
#     def speak(self):
#         print("Parent is speaking.")

# class Child(Parent):
#     def introduce(self):
#         print("Child is introducing.")

# my_child = Child()
# my_child.greet()  # Inheriting from Grandparent
# my_child.speak()  # Inheriting from Parent
# my_child.introduce()


# class A:
#     def method_a(self):
#         print("Method A from class A.")

# class B:
#     def method_b(self):
#         print("Method B from class B.")

# class C(A, B):
#     def method_c(self):
#         print("Method C from class C.")

# my_instance = C()
# my_instance.method_a()  # Inheriting from class A
# my_instance.method_b()  # Inheriting from class B
# my_instance.method_c()


# class  computer:
#     def __init__ (self):
#         self.__maxprice = 900
#     def sell(self):
#         print("sellino price: {}".format(self.__maxprice))
#     def setMaxPrice (self, price):
#         self.__maxprice = price
# c = computer()
# c.sell()

# c.__maxprice = 1000
# c.sell()

# c.setMaxPrice(1000)
# c.sell()


# class Polygon:
#     def render(self):
#         print("Rendering Polygon...")
# class square(Polygon):
#     def render(self):
#         print("Rendering square...")
# class circle(Polygon):
#     def render(self):
#         print("Rendering Circle...")
# s1 = square()
# s1.render()
# c1 = circle()
# c1. render()

