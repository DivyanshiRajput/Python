n= input ("amount= ")
a= (n-n%200)/200
b= n%200

c= (b- b%50)/50
d= b%50

e= (d- d%10)/10
f= d%10

g= (f- f%5)/5
h= f%5

i= (h -h%2)/2
j= h%2

A= a+c+e+g+i+j

print ("number of notes= " + str(A) )


