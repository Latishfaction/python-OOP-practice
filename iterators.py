'''User defined Range function with iterators'''
import clearterm


class def_range:
    def __init__(self):  # initialising starting and ending point
        self.val = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.val <= 10:
            current_val = self.val
            self.val += 1
            return current_val
        else:
            raise StopIteration


d1 = def_range()
for i in d1:
    print(i)
