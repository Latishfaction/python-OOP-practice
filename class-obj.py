import os
os.system('cls')
#######################################################################


class computer:
    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print("Config: ", self.cpu, self.ram)


com1 = computer('i5', '16 Ram')
com2 = computer('Ryzen8', '8 Ram')
com1.config()
com2.config()
