from Q1input import *

# Your code - begin
l= len(inp)
i=0
count=0
output= ""
prev= inp[0]

while (i<l):
	x= inp[i]
	if prev==x :
	 count += 1
	else:
	 output+=prev+str(count)
	 count= 1
	prev= x
	i+=1	
output+=prev+str(count)
# Your answer should be placed in this variable.
# Your code - end

print output
