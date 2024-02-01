import sys
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y= y
class Circle:
    def __init__(self, center, radius):
        self.center = Point(*center)
        self.radius = radius

    def contains(self, point:Point):
        if(((point.x - self.center.x)**2) + ((point.y - self.center.y)**2))**0.5 <= self.radius:
            return True
        else:
            return False
        
def main():
    if(len(sys.argv) != 3):
        print("Error")
        sys.exit(1)
    try:
        x = float(sys.argv[1])
        y = float(sys.argv[2])
    
        b = Point(x, y)
        a = Circle((0,0),1)

        if(a.contains(b)):
            print (f'The Point ({x}, {y}) lies in the Circle of center (0, 0) and radius 1')
        else:
            print ('The Point ({x}, {y}) lies out of the Circle of center (0, 0) and radius 1')
    except  ValueError:
        print("ONLY NUMBERS")
        return


if __name__ == "__main__":
    main()