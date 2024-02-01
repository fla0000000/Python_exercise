def ft_print():
    s = input("Inser a string: ")
    n = int(input("Insert an integer: "))
    i = len(s)
    if(n < i and n > 0):
        print(s[n], s[i - n])
    else:
        print("Error: index out of range")

ft_print()