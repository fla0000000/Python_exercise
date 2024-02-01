import sys
def ft_ext_pos():
    if(len(sys.argv) == 1):
        print("Error! Usage: python3 ft_ext_pos.py <x1> ... <xn>")
        sys.exit(1)
    num= []
    i = len(sys.argv) - 1
    y = 1
    while(y <= i):
        num += [int(sys.argv[y])]
        y+=1
    y -= 2
    nume = num[y]
    numo = num[y]
    while(y >= 0):
        if(nume < num[y]):
            nume = num[y]
            ix = y
        if(numo > num[y]):
            numo = num[y]
            iex = y
        y -= 1
    print("The min is ", numo, "and its position is ", iex)
    print("The max is ", nume, "and its position is ", ix)
    
ft_ext_pos()