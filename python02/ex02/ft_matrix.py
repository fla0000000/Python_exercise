import sys


def main():
    if len(sys.argv) != 3:
        print("Error! Usage: python3 ft_matrix.py <n> <m>")
        sys.exit(1)
    
    n = int(sys.argv[1])
    m = int(sys.argv[2])
    mat=[]
    x = 0

    while x < n:
        y =0
        matrix= []
        while y < m:
                val = float (input (f'Insert the element in position ({x}, {y}): '))
                matrix.append (val)
                y +=  1
        mat.append (matrix)
        x+=1
    print("The inserted matrix is:")
    for l in mat:
        print(l)

    x = 0
    sumrow= []
    while(x < n):
        sumr =0
        y = 0
        while(y < m):
            sumr+=mat[x][y]
            y+=1
        sumrow.append(sumr)
        x +=1

    y = 0
    ris1 = []
    while(y < m):
        sum = 0
        x = 0
        while(x < n):
              sum +=mat[x][y]
              x+=1
        ris1.append(sum)
        y+=1
    
    print("The sum over rows is:")
    print(sumrow)
    print("The sum over column is: ")
    print(ris1)


main()