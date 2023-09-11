class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @property
    def fahrenheit(self):
        return (self._celsius * 9/5) + 32

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature below absolute zero is not possible.")
        self._celsius = value

temp = Temperature(25)
print(temp.celsius)    # Output: 25
print(temp.fahrenheit) # Output: 77.0
temp.celsius = 30
print(temp.fahrenheit) # Output: 86.0



# class MyMeta(type):
#     def __init__(cls, name, bases, attrs):
#         print(f"Creating class {name} with attributes {attrs}")
#         super().__init__(name, bases, attrs)

# class MyClass(metaclass=MyMeta):
#     class_variable = 42

#     def __init__(self, value):
#         self.instance_variable = value

# obj = MyClass(10)
# # Output:
# # Creating class MyClass with attributes {'__module__': '__main__', 'class_variable': 42, '__init__': <function MyClass.__init__ at 0x...>, '__doc__': None}


