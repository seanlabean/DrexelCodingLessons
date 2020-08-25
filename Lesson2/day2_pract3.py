import math as m

# Sum numbers from 1/1 to 1/M

#prompt user
print("Hello! I'm going to compute a sum for you")
M = float(input("What is M?: "))
i = 1

sum = 0

while i <= M:
	sum += 1.0/i
	i += 1

print(sum)
