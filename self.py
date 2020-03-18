import clearterm


class computer:
    def __init__(self):
        self.name = 'Latish'
        self.age = 28

    def show(self):
        print('Name: ', self.name)
        print('Age: ', self.age)

    def compare(self, other):
        res = True if self.age == other.age else False
        return res


c1 = computer()  # Creating c1 as a object
c2 = computer()  # Creating c2 as a object
c2.age = 28
if c1.compare(c2):
    print("Same")
else:
    print('different')
