class ValidStrning:
    def __set_name__(self, owner, name):
        self.__name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.__name]

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError(f"{value} должно быть в формате str.")
        instance.__dict__[self.__name] = value


class Person:
    firstname = ValidStrning()
    lastname = ValidStrning()

    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def __str__(self):
        return f"{self.firstname} {self.lastname} {self.age}"

    @property
    def age_(self):
        return self.age

    @age_.setter
    def age_(self, new_age):
        if not isinstance(new_age, int):
            raise ValueError(f"{new_age} должен быть в формате int")
        self.age = new_age


p = Person('Tuychiyev', 'Baxtiyor', 26)
print(p)


class Integer:
    def __set_name__(self, owner, name):
        self.__name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.__name]

    def __set__(self, instance, value):
        if not isinstance(value, (int, float)):
            raise ValueError(f'{value} должен быть в формате int или float')
        instance.__dict__[self.__name] = value


class Order:
    name = ValidStrning()
    price = Integer()
    count = Integer()

    def __init__(self, name, price, count):
        self.name = name
        self.price = price
        self.count = count

    def __str__(self):
        return f"Name: {self.name}, price: {self.price}, count: {self.count}"


order = Order('apple', 1200, 20)
print(order)
print(order.__dict__)