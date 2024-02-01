import sys
def my_min(x = 0, y = 0, z = 0):
    if (x <  y and x < z):
       return x
    elif (y < x and y < z):
       return y
    elif (z < x and z < y):
        return z
    return 0

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Error! Usage: python3 ft_min.py <x> <y> <z>")
        sys.exit(1)
    num1 = sys.argv[1]
    num2 = sys.argv[2]
    num3 = sys.argv[3]

    mini = my_min(float(num1), float(num2), float(num3))
    print("The min is: ", mini)
