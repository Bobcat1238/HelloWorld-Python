class Human:
    def __init__(self, name, gender):
        super().__init__()
        self.name = name
        self.gender = gender

    def ShowCharacteristicts(self):
        print(f"This human's name is {self.name}.")
        print(f'This human is a {self.gender}.')


class Person(Human):
    """     def __init__(self, name):
            super().__init__()
            self.name = name """

    def Talk(self):
        print()
        print(f'Hello, my name is {self.name}')
        print()


aPerson = Person(gender='male', name='Cheech')
anotherPerson = Person('Chong', 'male')
aPerson.Talk()
aPerson.ShowCharacteristicts()
anotherPerson.ShowCharacteristicts()


