from numbers import Number

class Circle:

    def __init__(self, c, r):
        if not (isinstance(c, tuple) and len(c) == 2):
            raise ValueError("Please provide centre as tuple of two numbers!")
        
        for i in c:
            if not isinstance(i, Number):
                raise ValueError("Please provide number for center!")

        self.centre = c
        
        if not(isinstance(r, Number)):
            raise ValueError("Please provide radius as a number!")

        self.radius = r
        

    def __contains__(self, point):

        centered = (point[0] - self.centre[0], point[1] - self.centre[1])

        distance = pow(centered[0], 2) + pow(centered[1], 2)

        if distance <= pow(self.radius, 2):
            return True

        else:
            return False
        
