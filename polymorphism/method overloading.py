'''Method overloading: Python does not have the concept of method overloading (same function name inside a class) because if you write the same function inside a class ,python will interpret only the last function 
'''
'''But we can achieve method overloading by function arguments by calling them and also set define the variable in the parameter of the function'''


def ss(a=None, b=None, c=None):
    if a != None and b != None and c != None:
        s = a+b+c
    elif a != None and b != None:
        s = a+b
    else:
        s = a
    return s


print(ss(5, 5))
