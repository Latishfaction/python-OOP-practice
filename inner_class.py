'''Inner class: In python we can use class inside  a class'''
import clearterm


class student:  # OUTER CLASS
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
        self.l1 = self.laptop()  # OBJECT OF INNER CLASS

    def show(self):
        print(self.name, self.roll)
        self.l1.show()  # call method of inner class function

    class laptop:  # innner class
        def __init__(self):
            self.brand = 'Asus'
            self.chip = 'i7'
            self.ram = 8

        def show(self):
            print(self.brand, self.chip, self.ram)


s1 = student('Navin', 28)
s2 = student('Ram', 39)
s1.show()
# lap = s1.laptop() # possible to call inner class from outside of the class
# lap.show() #possible to call innere class show function() from outside the class
