import math

class Point:
    def reset(self):
        self.x = 0
        self.y =0

    def move(self,x,y):
        self.x = x
        self.y = y

    def claculate_distance(self,other_point):
        return math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)

point1 = Point()
point2 = Point()

point1.reset()
point2.move(5,0)

print(point2.claculate_distance(point1))

assert (point2.claculate_distance(point1) == point1.claculate_distance(point2))

point1.move(3,4)
print(point1.claculate_distance(point2))
print(point1.claculate_distance(point1))