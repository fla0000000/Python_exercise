import sys

def ft_compare():
    if len(sys.argv) != 3:
        print("Usage: <arg1> <arg2>")
        sys.exit(1)
    num1 = sys.argv[1]
    num2 = sys.argv[2]

     
    if(num1 > num2):
        print(float(num1), " is greater than " ,float(num2))
    elif(num1 < num2):
        print(float(num1), " is less than ", float(num2))
    elif(num1 ==  num2):
        print(float(num1), " is equal to " ,float(num2))

ft_compare()