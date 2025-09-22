"""
oop_assignment.py
PLP Africa — Week 5 Day 2 (Object Oriented Programming)
Author: Student Name
Description:
 - Demonstrates class design, constructors, encapsulation, inheritance, and polymorphism.
 - Part 1: Custom classes (Book, EBook, Smartphone) with encapsulation and inheritance.
 - Part 2: Polymorphism challenge using Vehicle base class and Car/Plane/Boat subclasses.
"""

# ------------------ Part 1: Class Design (Book, EBook, Smartphone) ------------------

class Book:
    """A simple Book class demonstrating attributes, methods, and encapsulation."""
    def __init__(self, title: str, author: str, pages: int, isbn: str):
        self.title = title
        self.author = author
        self.pages = pages
        # private attribute (encapsulation)
        self.__isbn = isbn

    @property
    def isbn(self):
        """Read-only access to the private ISBN attribute."""
        return self.__isbn

    def read(self, pages: int = 1):
        """Simulate reading some pages of the book."""
        if pages <= 0:
            return f"Nothing read from '{self.title}'. Provide a positive page count."
        return f"You read {pages} page(s) of '{self.title}' by {self.author}."

    def __str__(self):
        return f"Book(title='{self.title}', author='{self.author}', pages={self.pages})"

class EBook(Book):
    """EBook extends Book and adds file-size and download behavior."""
    def __init__(self, title: str, author: str, pages: int, isbn: str, file_size_mb: float):
        super().__init__(title, author, pages, isbn)
        self.file_size_mb = file_size_mb

    def download(self):
        return f"Downloading '{self.title}' ({self.file_size_mb} MB)... Download complete."

    def __str__(self):
        return f"EBook(title='{self.title}', author='{self.author}', size={self.file_size_mb}MB)"

class Smartphone:
    """Smartphone class showing encapsulated battery level and methods to interact."""
    def __init__(self, brand: str, model: str, storage_gb: int):
        self.brand = brand
        self.model = model
        self.storage_gb = storage_gb
        # private attribute, encapsulated
        self.__battery_level = 100  # percentage

    @property
    def battery_level(self):
        """Safe read access to battery level."""
        return self.__battery_level

    def use_app(self, minutes: int):
        """Simulate using an app that drains battery (2% per minute)."""
        if minutes <= 0:
            return "No usage recorded."
        drain = minutes * 2
        self.__battery_level = max(0, self.__battery_level - drain)
        return f"Used phone for {minutes} minute(s). Battery now at {self.__battery_level}%."

    def charge(self, percent: int):
        """Charge the phone by a given percent (safe bounds)."""
        if percent <= 0:
            return "Charge percent must be positive."
        self.__battery_level = min(100, self.__battery_level + percent)
        return f"Charged {percent}%. Battery now at {self.__battery_level}%."

    def __str__(self):
        return f"Smartphone({self.brand} {self.model}, {self.storage_gb}GB)"

# ------------------ Part 2: Polymorphism (Vehicle classes) ------------------

class Vehicle:
    """Abstract-ish base class for vehicles. Subclasses implement move()."""
    def __init__(self, make: str, model: str):
        self.make = make
        self.model = model

    def move(self):
        raise NotImplementedError("Subclasses must implement move() method.")

    def __str__(self):
        return f"{self.make} {self.model}"

class Car(Vehicle):
    def __init__(self, make: str, model: str, wheels: int = 4):
        super().__init__(make, model)
        self.wheels = wheels

    def move(self):
        return f"{self} is driving on the road with {self.wheels} wheels."

class Plane(Vehicle):
    def __init__(self, make: str, model: str, engines: int = 2):
        super().__init__(make, model)
        self.engines = engines

    def move(self):
        return f"{self} is flying through the sky with {self.engines} engines."

class Boat(Vehicle):
    def __init__(self, make: str, model: str, hull_type: str = 'Planing'):
        super().__init__(make, model)
        self.hull_type = hull_type

    def move(self):
        return f"{self} is sailing on water (hull: {self.hull_type})."

# ------------------ Demonstration / test run ------------------

def demo():
    print('\n=== Part 1: Classes, Inheritance & Encapsulation Demo ===')
    # Books
    book = Book('The Little Prince', 'Antoine de Saint-Exupéry', 96, '978-0156012195')
    ebook = EBook('Python Tricks', 'Dan Bader', 250, '978-1775093305', 5.2)
    print(book)
    print(ebook)
    print(book.read(10))
    print(ebook.download())
    # trying to access private attribute (should not be accessed directly)
    try:
        print('Attempting to access private ISBN:', book.__isbn)
    except AttributeError as e:
        print('Cannot access private attribute directly: AttributeError raised as expected.')
    # but property works
    print('ISBN via property:', book.isbn)

    print('\nSmartphone demo:')
    phone = Smartphone('Nokia', 'XR-2025', 128)
    print(phone)
    print(phone.use_app(5))
    print(phone.charge(10))
    # show that private battery is accessible via name-mangling (not recommended)
    print('Battery via property (recommended):', phone.battery_level)
    print('Battery via name-mangled attribute (not recommended):', getattr(phone, '_Smartphone__battery_level'))

    print('\n=== Part 2: Polymorphism Demo (Vehicles) ===')
    car = Car('Toyota', 'Corolla', wheels=4)
    plane = Plane('Boeing', '737', engines=2)
    boat = Boat('Yamaha', '242X', hull_type='V-shaped')
    vehicles = [car, plane, boat]

    # Polymorphism: call move() on each vehicle without checking its type
    for v in vehicles:
        print(v.move())

    print('\nPolymorphism allows treating different vehicle objects uniformly:')
    # We can also pass them to functions that expect a Vehicle
    def travel(veh: Vehicle):
        # This function relies only on the common interface (move)
        return f'--> travel(): {veh.move()}'

    for v in vehicles:
        print(travel(v))

if __name__ == '__main__':
    demo()
