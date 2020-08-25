import math as m

#Print cos(x) to a file in pairs

#setup for  x values
dx = 0.1
start = 0
stop = 2*m.pi
N = (stop - start) / dx

#create writeable file
input_file = open('cos_vals.txt', 'w')


#get values and store them
print('printing values')
print('X values, Cos(X) values', file=input_file)

while start < stop:
	y_val = m.cos(start)
	#input_file.write(str(round(start,ndigits=2))+' '+str(y_val)+'\n')
	print(str(round(start,ndigits=1))+' '+str(y_val),file=input_file)
	start += dx

#CLOSE THE FILE
input_file.close()
print('All Done')
