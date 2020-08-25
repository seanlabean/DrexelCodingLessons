#Read in the file 'block_data.txt' using either loadtxt or genfromtxt. 
#Print month and year that made the most money

#import numerical python 
import numpy as np

#import file into list
file_name = 'block_data.txt'
month = np.genfromtxt(file_name, usecols=[0], dtype='str')
years, money = np.loadtxt(file_name, usecols=[1,2], dtype='int', unpack=True)

max_val = max(money)
index = list(money).index(max_val)

print("The most money was earned in %s, %d which was $%dk" % (month[index], years[index], money[index]))
