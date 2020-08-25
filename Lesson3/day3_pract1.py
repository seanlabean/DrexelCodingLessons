#Read words from words.txt into a list and sort that list

import string

#Read in the file

#filename = input("What file would you like sorted?: ")
input_file = open('words.txt')
#input_file = open(filename)

#create empty lists
lines = []

for line in input_file:
	#append the line in the file to the list
	lines.append(line.strip('\n'))	
	#sort the lines alphabetically
	lines.sort()

print(lines)

#Good practice to close file after finished!
input_file.close()
