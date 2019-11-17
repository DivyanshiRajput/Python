import math
a= input ("side 1: ")
b= input ("side 2: ")
H= math.sqrt(a*a + b*b)

if (a>0) and (b>0):
   print  ("hypotenuse= " + str(H))

else:
   print  ("invalid input") 
