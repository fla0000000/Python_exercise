import sys
def ft_max():
    if len(sys.argv) != 4:
        print("Error! Usage: python3 ft_max.py <x> <y> <z>")
        sys.exit(1)
    num1 = sys.argv[1]
    num2 = sys.argv[2]
    num3 = sys.argv[3]

     
    if(num1 > num2 and num1 > num3):
        print("The max is:" ,float(num1))
        sys.exit(1)
    elif(num3 > num2 and num3 > num1):
        print("The max is:" ,float(num3))
        sys.exit(1)
    elif (num2 > num1 and num2 > num3):
       print("The max is:" ,float(num2))
       sys.exit(1)

ft_max()