class Person:
    def __init__(self, name):
        super().__init__()
        self.name = name

    def Talk(self):
        print(f'Hello, my name is {self.name}')


aPerson = Person('Cheech')
aPerson.Talk()
