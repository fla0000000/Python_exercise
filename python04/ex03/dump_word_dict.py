import pickle

if __name__ == "__main__":
    word_length_count = {}
try:
    file = open('words.txt')
    list = file.read()
    conte = list.split()
    for line in conte:
        length = len(line)
        if(length in word_length_count):
                word_length_count[length]+= 1
        else:
                word_length_count[length] = 1
    with open('word_count.pickle', 'wb') as pickle_file:
        pickle.dump(word_length_count, pickle_file)
        # print("hello")
        # for key, value in pickle.dump(word_length_count, pickle_file):
        #     print(f'{key},{value}')
except FileNotFoundError:
    print("Error! The specified file does not exist!")
