'''Instead of using dictionary, we can use a "namedTuple" than regular tuple, but it only apply when we don't change the attributes '''
import clearterm
from collections import namedtuple  # import namedTuple

Color = namedtuple('Color', ['red', 'blue', 'green'])  # declaring namedTuple
color = Color(233, 445, 664)  # creating tuple refering to namedTuple
White = Color(1, 2, 3)  # creating another tuple refering to namedTuple
print(color.green)
# to access namedTuple enter {tuple-name.namedTuple-Attribute}
