'''When we paas diffrent argument in the function so it should have diffrent behaviour as per the input'''
import clearterm
'''NOTE: THIS NEED TO REVIEW'''


class duck:
    def data(self):
        print(duck.__name__)
        print('I am Duck')


class horse:
    def data(self):
        print(horse.__name__)
        print("I am a Horse")


class human:
    def human(self):
        print(human.__name__)
        print("I am human")


def fun(obj):  # this function doesn't care from which class is the object is coming from, it's just know that it has to a task with the help of an object which we are passing as a parameter
    if hasattr(obj, 'data'):
        obj.data()  # checks the function "data" from the passing object
    else:
        obj.human()  # else from other function


d1 = duck()
fun(d1)
