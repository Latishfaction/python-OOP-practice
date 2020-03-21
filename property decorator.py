'''Property decorator: We can call a function as a attribute instead of calling a function()'''
'''Also we can get and set the value using property decorator'''




import clearterm
class Emp:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return self.first+" "+self.last+"@gmail.com"

    @email.deleter
    def email(self):
        print('Email deleted!')

    @property
    def fullname(self):
        return self.first+" "+self.last

    @fullname.setter
    def fullname(self, name):
        first, last = name.split()
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Successfully Deleted!')
        self.first = None
        self.last = None


e = Emp("Jim", 'Corey')
e.fullname = "Hello World"

print(e.first)
print(e.fullname)
print(e.email)
del e.fullname
del e.email
