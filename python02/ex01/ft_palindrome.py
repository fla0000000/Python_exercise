import sys
def is_palindrome(x):
    i = len(x) -1
    j = 0
    while i > j and i != j:
        if x[j] == " ":
            j+=1
        if x[i] == " ":
            i-=1
        if(x[i] != x[j]):
            return False
        j+=1
        i-=1
    return  True



if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Error! Insert just 1 string!")
        sys.exit(1)
    str = sys.argv[1]
    bool = is_palindrome(str)
    if(bool == True):
        print("The string", str ,"is palindrome")
    else:
        print("The string", str ,"is not palindrome")