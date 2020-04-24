'''Whenever a class runs it calls the __init__ method, if a class doesn't have __init__ method so it calls the __init__ method of super-class'''

'''Method Resolution Order(MRO): It generally happens in 'Multiple-Inheritance', When we encounter same method name(including __init__) in the both of the super class, then it execute from left-to-right '''

'''super(): If want to call a super-class method from it's sub-class then we use super() method and it can be used in __init__ function and normal functions'''


class a:
    def __init__(self):
        print("Init A:")

    def feature1(self):
        print('This is feature 1-a')

    def feature2(self):
        print('This is feature 2')


class b:
    def __init__(self):
        print("Init B:")

    def feature1(self):
        print('This is feature 1-b')

    def feature4(self):
        print('This is feature 4')


class c(a, b):

    def feature1(self):
        print('This is feature 5')

    def feature6(self):
        print('This is feature 6')


# cb = b()
cc = c()
cc.feature1()
