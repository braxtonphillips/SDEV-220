"""
Braxton Phillips
SDEV 220
Chapter 12 Exercise 12.1
Due Nov 21, 2020
"""

class GeometricObject:
    def __init__(self, color = '', filled=True):
        self.color = color
        self.filled = filled

    def getColor(self):
        return self.color

    def setColor(self, color): 
        self.color = color

    def isFilled(self):
        return self.filled

    def setFilled(self, filled):
        self.filled = filled

    def __str__(self):
        return 'Color: %s and Filled: %s' % (self.color, str(self.filled)) #gets color and filled stat and reyurns in printed vals in main


class Triangle(GeometricObject):
    def __init__(self, s1 = 0.0, s2 = 0.0, s3 = 0.0, color = '', filled = True):
        super().__init__(color, filled)
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
    
        #A = 1/2(b * h)
    def getArea(self):
        trianglePerimeter = self.getPerimeter() / 2
        return (trianglePerimeter * (trianglePerimeter - self.s1) * (trianglePerimeter - self.s2) * (trianglePerimeter - self.s3)) ** 0.5

    def getPerimeter(self):
        return self.s1 + self.s2 + self.s3


def main():
    s1 = s2 = s3 = 2
    print('The values for all sides are 2.')

    #getting user input
    color = input('Enter color of the triangle: ') 
    filled = input('Is the triangle filled? 1 - yes or 0 - no: ') 
    filled = (filled == "1") #binary choice to see if user filled tri 
    triangleVals = Triangle(s1, s2, s3, color, filled) #sends user input to tri class 

    print(triangleVals)
    #using formatting for output
    print('Area: ',"%.2f" % triangleVals.getArea(), 'Perimeter: ',"%.2f" % triangleVals.getPerimeter()) 

main()