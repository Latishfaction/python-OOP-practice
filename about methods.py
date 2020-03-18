import clearterm
'''instance methods, class methods, static me'''


class student:
    school = "Faction"  # class variable / static variable

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):  # instance method (self) constructor inside
        return (self.m1+self.m2+self.m3)/3  # instance variable

    @classmethod
    def getsch(cls):  # class method (cls) constructor inside
        return cls.school

    @staticmethod  # static method
    def info():
        print("This can use out of class")


s1 = student(22, 33, 55)
s2 = student(67, 20, 33)
print("SCHOOL: ", student.getsch())
print("S1: ", s1.m1, s1.m2, s1.m3)
print("Avg:", s1.avg())
print("S2: ", s2.m1, s2.m2, s2.m3)
print("Avg:", s2.avg())
student.info()
