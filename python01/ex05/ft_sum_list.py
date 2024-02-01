import sys

def ft_sum(numbers, i):
    res = numbers[i]
    return int(res)

def ft_sum_list():
    numbers = []
    i = 0
    result = 0
    while True:
            user_input = int(input("Insert integer: "))
            
            # Break the loop if the user enters 0
            if user_input == 0:
                break

            # Add the entered integer to the list
            numbers+=[user_input]
            i+=1
    while(i > 0):
        i-=1
        result += ft_sum(numbers, i)
    print("The sum is: ", result)

ft_sum_list()