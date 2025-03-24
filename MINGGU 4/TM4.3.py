from abc import ABC, abstractmethod

# Abstraction: Abstract class Animal
class Animal(ABC):
    def __init__(self, name: str, age: int):
        if not name:
            raise ValueError("Nama hewan tidak boleh kosong!")
        if age <= 0:
            raise ValueError("Usia hewan harus lebih dari 0!")
        
        self.__name = name  # Encapsulation (Private Attribute)
        self.__age = age
    
    @abstractmethod
    def make_sound(self):
        pass
    
    # Getter
    def get_info(self):
        return f"Nama: {self.__name}, Usia: {self.__age} tahun"
    
    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    # Setter
    def set_name(self, name: str):
        if not name:
            raise ValueError("Nama tidak boleh kosong!")
        self.__name = name

    def set_age(self, age: int):
        if not isinstance(age, int):
            raise ValueError("Usia harus bilangan bulat!")
        if age <= 0:
            raise ValueError("Usia harus lebih dari 0!")
        self.__age = age

# Inheritance & Polymorphism: Subclasses dengan suara berbeda
class Dog(Animal):
    def make_sound(self):
        return "Guk guk!"

class Cat(Animal):
    def make_sound(self):
        return "Miaw Miaw Miaw"

class Lion(Animal):
    def make_sound(self):
        return "Rawrrr"
    
# Contoh Penggunaan
dog = Dog("Doggy", 2)
print(dog.get_info())  # Output: Nama: Doggy, Usia: 2 tahun
print("Suara :", dog.make_sound())  # Output: Guk guk!

cat = Cat("Kitty", 1)
print(cat.get_info())  # Output: Nama: Kitty, Usia: 1 tahun
print("Suara :", cat.make_sound())  # Output: Miaw Miaw Miaw

lion = Lion("Lionel", 3)
print(lion.get_info())  # Output: Nama: Lionel, Usia: 3 tahun
print("Suara :", lion.make_sound())  # Output: Rawrrr

# Uji Setter
print("\nUji Setter Age:")
try:
    dog.set_age(4)
    print("Set age sukses:", dog.get_info())  # Output: Nama: Doggy, Usia: 4 tahun
except ValueError as e:
    print("Error:", e)

try:
    dog.set_age(-1)  # Seharusnya error
except ValueError as e:
    print("Error:", e)  # Output: Usia harus lebih dari 0!