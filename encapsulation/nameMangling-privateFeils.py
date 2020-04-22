'''Encapsulation: Name Mangling and Private Feilds '''

'''Private Feilds: To make the initialization to private variable so that we can not access it directly but we can access it from function and make use of that variable and also through "name mangling"'''

'''Name Mangling: It is th method to access the variables in private feilds'''

class Employee:
    def __init__(self):
        #used __(underscore-before variable name) to make the variables private
        self.__name="Josh"
        self.__id=7
    def display(self):
        #accessing private feild variable by using them in a method
        self.__name='Kash'
        print(self.__name)
        print(self.__id)
        
emp=Employee()

print('"Traditional Method"')
emp.display() #calling display (method) to show the private feilds variable
print()
print('"Name Mangling"')
print(emp._Employee__name) #accessing through Name Mangling
print(emp._Employee__id)   #accessing through Name Mangling