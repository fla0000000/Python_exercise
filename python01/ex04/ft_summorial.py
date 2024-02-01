import sys
def ft_summorial():
    if(len(sys.argv) != 2):
        print("Error! Usage: python3 ft_summorial.py <n>")
        sys.exit(1)
    num = sys.argv[1]
    if(int(num) < 0):
        print("Error! n must be >=0")
        sys.exit(1)
    i = 0
    j = 0
    while(i < int(num)):
        i+=1
        j+=i
    print("The sum is: ", j)


ft_summorial()

