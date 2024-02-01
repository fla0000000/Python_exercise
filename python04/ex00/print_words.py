def sort(array):
	j = 0
	while(j < len(array)-1):
		i = 0
		while(i < len(array) - 1):
			if array[i]>array[i+1]:
				array[i], array[i+1] = array[i+1], array[i]
			i+=1
		j+=1
		

get = open("words.txt")
num = int(input("Insert an integer: "))
list = []
for x in get:
	if (len(x) > num):
		list.append(x)
sort(list)
print(f'The words longer than {num} are the following:')
for l in list:
	print(l, end ="")
