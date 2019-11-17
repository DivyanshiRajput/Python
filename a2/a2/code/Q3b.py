from Q3input import *

# Your code - begin
output=[]
i=0
while (i<len(m1[0])):
	a=[]
	j=0
	while (j<len(m1)):
		a.append(0)
		j+=1
	output.append(a)
	i+=1
for x in range(len(m1)):
	for y in range(len(m1[0])):
	   output[y][x]=m1[x][y]
# Your code - end
print output
