class MyClass:
    def __init__(self):
        self.public_atrr = "I'm public"        # 0 guión bajo
        self._protected_attr = "I'm protected" # 1 guión bajo
        self.__private_attr = "I'm private"    # 2 guiones bajos

my_obj = MyClass()

# miembro público accesible
print(my_obj.public_atrr)

# miembro privado accesible
print(my_obj._protected_attr)

# miembro privado accesible via name decoration
print(my_obj._MyClass__private_attr)
