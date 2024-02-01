def ft_print():
    s = input("Inser a string:")
    n = int(input("Insert an integer: "))
    print(len(s))
    if(n <= len(s)):
        print(s[n:-n + 1])
    else:
        print("Error: index out of range")

ft_print()