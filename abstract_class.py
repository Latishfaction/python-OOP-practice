'''Abstract Method: those methods who doesn't have any body '''

'''Abstract Class: Where the "abstract method" is defined '''
'''NOTE: We can not create object of abstract class but we can define abstract class in it's child class '''




import clearterm
from abc import ABC, abstractmethod
class computer(ABC):  # defining abstract class
    @abstractmethod  # defining '@abstractmethod' decorator for abstract class
    def process(self):
        pass


class laptop(computer):
    def process(self):
        print('this is running')


l1 = laptop()
l1.process()
