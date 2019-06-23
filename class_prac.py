class Human():
    abc = 10
    def __init__(self, name='John Doe'):
        self.name = name
        self.favourite_dish = 'Not yet set'
        print('I am constructor')

    def set_favourite_dish(self, favourite_dish):
        self.favourite_dish = favourite_dish

print(Human.abc)
h1 = Human()
h2 = Human('Inam')
h3 = Human()
h4 = Human()
print(h1.name)
print(h2.name)
h2.name = 'Abdulhaq'
print(h2.name)
print(h2.favourite_dish)
h2.set_favourite_dish('Biryani')
print(h2.favourite_dish)
