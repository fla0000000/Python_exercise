
def ft_sum_time():
    hours = input("Insert hours: ")
    minutes = input("Insert minutes: ")
    seconds = input("Insert seconds: ")

    total = int (hours) * 60 * 60 + int(minutes) * 60 + int(seconds)
    print("Total seconds: ", total)

ft_sum_time()