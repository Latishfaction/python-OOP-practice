'''note:need to review '''


class student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1 = self.m1+other.m1
        m2 = self.m2+other.m2
        total = student(m1, m2)
        return total


s1 = student(5, 5)
s2 = student(15, 25)
s3 = s1+s2
print(s3.m1)
print(s3.m2)
