class Person:
    def __init__(self, name: str):
        self.name = name

    # create the method greet here
    def greet(self) -> str:
        return f"Hello, I am {self.name}!"


test_person = Person(input())
print(test_person.greet())
