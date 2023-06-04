import math
class Point:
    def __init__(self, x_value, y_value=0 , z_value=0):
        # Maximum value
        MAX_VAL = 10000

        # Minimum value
        MIN_VAL = -10000
        self.MAX_VAL = MAX_VAL
        self.MIN_VAL = MIN_VAL
        if not 0 <= x_value <= self.MAX_VAL:
            print ('Invalid x_value')
        if not 0 <= y_value <= self.MAX_VAL:
            print ('Invalid y_value')
        if not 0 <= z_value <= self.MAX_VAL:
            print ('Invalid z_value')
        self._x_value = x_value
        self._y_value = y_value
        self._z_value = z_value
        
    def get_x_value(self):
        return self._x_value

    def get_y_value(self):
        return self._y_value

    def get_z_value(self):
        return self._z_value

    def __str__(self):
        if self._x_value == 0.1:
            self._y_value = 0
            self._z_value = 0
        return 'Point(x_value = {}, y_value = {}, z_value = {})'.format(self._x_value, self._y_value, self._z_value)
    
    def get_distance_between_points(self, other_point = None):
        if other_point == None:
            dist = math.sqrt((self._x_value)**2 + (self._y_value)**2 + (self._z_value)**2)
        elif self._x_value == 0.1 and other_point == None:
            dist = self._x_value
        else:
            dist = math.sqrt((self._x_value-other_point._x_value)**2 + (self._y_value-other_point._y_value)**2 + (self._z_value-other_point._z_value)**2)
        return 'Distance is {}'.format(dist)
a = Point(1,math.sqrt(2),1)
print(a)
b = a.get_distance_between_points(Point(1, math.sqrt(2), 0))
print(b)
c = a.get_distance_between_points()
print(c)      
            