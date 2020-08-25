import math as m

#choose variables
x = float(input("Choose x: "))
m_var = float(input("Choose m: "))
s = float(input("Choose s: "))
print("x is %d" % x)
print("m is %d" % m_var)
print("s is %d" % s)

#calculate
f = (1./m.sqrt(2 * m.pi)) * m.exp(-1*(1./2)*(((x-m_var)/float(s))**2))

#print answer
print("therefore, the Guassian is computed as")
print(f)

