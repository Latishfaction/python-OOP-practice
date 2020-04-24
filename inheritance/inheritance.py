


class a:
    def feature1(self):
        print('This is feature 1')

    def feature2(self):
        print('This is feature 2')


class b:
    def feature3(self):
        print('This is feature 3')

    def feature4(self):
        print('This is feature 4')


class c(a, b):
    def feature5(self):
        print('This is feature 5')

    def feature6(self):
        print('This is feature 6')


cc = c()
cc.feature6()
