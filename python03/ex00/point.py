class Point:

    def __init__(self, x, y):
        self.x=x
        self.y=y
    
    def ft_check(n):
        c = n.index(',')
        f =Point(float(n[c + 1:]), float(n[:c]))
        l = f.x - f.y
        return l

    def point():
        xy1 = input("Insert the coordinates of the first point: ")
        xy2 = input("Insert the coordinates of the second point: ")
        x = Point.ft_check(xy1)
        y = Point.ft_check(xy2)
        risult = (x**2 + y**2)**0.5
        print("Their distance is: ", risult)


if __name__ == "__main__":
    Point.point()