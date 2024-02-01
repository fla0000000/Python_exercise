import sys

def trim(input_list):
    return None

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print ('Error! You must insert at least 2 values'),
    else:
        print ('The new list is:'),
        print(sys.argv[2:-1])

