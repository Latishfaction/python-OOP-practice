import clearterm

'''Class Variable and Instance Variable'''


class car:
    wheels = 4  # class variable

    def __init__(self):
        self.name = 'BMW'  # instance variable
        self.color = 'blue'  # instance variable


c1 = car()
c2 = car()
print(c1.name)
print(c1.color)
print(c1.wheels)
print('"C2"')
print(c2.name)
print(c2.color)
print(c2.wheels)
