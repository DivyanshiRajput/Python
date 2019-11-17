from Q3input import *

# Your code - begin
output=[]
i=0
while (i<len(m1)):
	a=[]
	j=0
	while (j<len(m2[0])):
		a.append(0)
		j+=1
	output.append(a)
	i+=1
r1= len(m1)
r2= len(m2)
c1= len(m1[0])
c2= len(m2[0])
if (r2==c1):
	i=0
	while (i<len(m1)):
	  j=0
	  while (j<len(m2[0])):
	    k=0
	    while (k<len(m2)):
		output[i][j]+=(m1[i][k]*m2[k][j])
		k+=1
	    j+=1
	  i+=1
else:
	print ("cannot be multiplied")

# Your code - end
print output
