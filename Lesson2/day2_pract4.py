import math as m 

#Store odd numbers from 1 to N in a list

#prompt user for N
N = int(input("Give me an integer greater than 1, please "))

odd = list(range(1, N+1, 2))

print("Here is a sorted list of odd numbers from 1 to N")
print(odd)

