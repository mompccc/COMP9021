# Defines two classes, Point() and NonVerticalLine().
# An object for the second class is created by passing named arguments,
# point_1 and point_2, to its constructor.
# Such an object can be modified by changing one point or both points thanks to the
# function change_point_or_points().
# At any stage, the object maintains correct values for slope and intersect.
#
# Written by *** and Eric Martin for COMP9021


class Point():
    def __init__(self, x = None, y = None):
        if x == None and y == None:
            self.x = 0
            self.y = 0
        elif x == None or y == None:
            print('Need two coordinates, point not created.')
        else:
            self.x = x
            self.y = y

class NonVerticalLine:
    def __init__(self, *, point_1, point_2):
        if not self._check_and_initialise(point_1, point_2):
            print('Incorrect input, line not created.')
            return

    def change_point_or_points(self, *, point_1 = None, point_2 = None):
        if not self._change_point_or_points(point_1, point_2):
            print('Could not perform this change.')
            return

    def _check_and_initialise(self, p1, p2):
        if p1.x==p2.x:
            return False
        else:
            self._slope(p1, p2)
            self._intercept(p1, p2)
            self.point_1=p1
            self.point_2=p2
            return True
        # Replace this comment with your code

    def _change_point_or_points(self, p1, p2):
        if p1==None and p2!=None:
            if p2.x!=self.point_1.x:
                self.point_2=p2
                self._slope(self.point_1, self.point_2)
                self._intercept(self.point_1, self.point_2)
                return True
            else:
                return False
        elif p2==None and p1!=None:
            if p1.x!=self.point_2.x:
                self.point_1=p1
                self._slope(self.point_1, self.point_2)
                self._intercept(self.point_1, self.point_2)
                return True
            else:
                return False
        elif p1!=None and p2!=None:
            if p2.x!=p1.x:
                self.point_1=p1
                self.point_2=p2
                self._slope(self.point_1, self.point_2)
                self._intercept(self.point_1, self.point_2)
                return True
            else:
                return False
        else:
            return True
        # Replace this comment with your code

    def _slope(self, p1, p2):
        self.X = p1.x -p2.x
        self.Y = p1.y -p2.y
        self.slope = self.Y/self.X
        if self.slope == -0.0:
            self.slope = 0.0

    def _intercept(self, p1, p2):
        self.intercept=p1.y - self.slope * p1.x
    # Possibly define other functions
        

            
            
