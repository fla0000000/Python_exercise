import sys


def sort(array):
	j = 0
	while(j < len(array)-1):
		i = 0
		while(i < len(array) - 1):
			if array[i]>array[i+1]:
				array[i], array[i+1] = array[i+1], array[i]
			i+=1
		j+=1
		
if len(sys.argv) != 2:
	print("Error! No string given")
	sys.exit(1)
print("Char count:")
list = []
for i in sys.argv[1]:
    if (i not in list):
        list.append(i)
sort(list)
dixt = dict()
for j in list:
		temp = 0
		for i in sys.argv[1]:
			if (j == i):
				temp += 1 
		dixt[j] = temp

for key, value in dixt.items():
      print(f'{key} = {value}')