from copy import deepcopy

pot = [2**i for i in range (0,100)]
print (pot)

b = a = [ "ich", "mag", "Kuchen"]
c = a[:]
d = deepcopy(a)
b[1] = "hasse"
c[2] = "Orange"
print ( a)
print (b)
print (c)
print (d)

squars = { i: i**2 for i in range (0,100)}
print (squars)
keys = [i for i in squars]
print (keys)

evan = [i for i in range(1,100) if i%2==0]
print (evan)

def degToFahr(deg):
    return deg * 1.8 + 32

print ("fahrenheit:")
fahrenheit = list(map(degToFahr, range(1,101)))
print (fahrenheit)

highTemp = filter( lambda x: x > 100 , fahrenheit)
print (sum(highTemp))

def revList(list):
    return list[::-1]

print (list(revList(range(1,100))))

x = [i for i in range(1,10)]
y = [i for i in range(4,13)]
print (x,y)
points = [(x[i], y[i]) for i in range (0,len(x))]
print (points)
xPos = [points[i][0] for i in range (0, len(points))]
yPos = [points[i][1] for i in range (0, len(points))]
print (xPos, yPos)

class Point:
    def __init__(self, x, y):
        self.X = x;
        self.Y = y;
    def setXY(self, x, y):
        self.X = x
        self.Y = y;
    def getXY (self):
        return self.X, self.Y
    def dist(self, point):
        from math import sqrt
        return sqrt( (self.X-point.X)**2 + (self.Y - point.Y) **2)
print (Point(0,0).dist(Point(1,1)))

class Face:
    def __init__(self, name, color): 
        self.Name = Name
        self.Color = color
    def area(self) : ...
    def extent(self) : ...
    
class rect(Face):
    def area(self):
        from math import sqrt
        return sqrt(self.X*self.Y)
    def extent(self):
        return self.X*2+self.Y*2
        


