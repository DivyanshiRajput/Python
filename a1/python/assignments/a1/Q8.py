print ("1.add")
print ("2.multiply")
print ("3.average")

choice= input ( "enter choice(1/2/3): ")
n= input ("enter first number: ")
m= input ("enter second number: ")

a= (n+m)/2.0
b= (n+m)
c= n*m

if (choice == 1):
   print "sum" , (b)

elif (choice == 2):
   print "product", (c)

elif (choice == 3):
   print "average", (a)
