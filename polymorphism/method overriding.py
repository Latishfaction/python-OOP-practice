'''Method overiding: same function, arguments(in-function) but different operation'''
import clearterm

class A:
    def show(self):
        print('Show in A')


class B(A):
    def show(self):
        print('Show in B')


a1 = B()
a1.show()  # checks show() in B if present then perform that function
# if show() not present on b then  it will check it's parent class
