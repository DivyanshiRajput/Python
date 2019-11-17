from Q7input import *

# Your code - begin
l1.extend(l2)
i=1
while (i<len(l1)):
	j= i-1
	key= l1[i]
	while (j>=0 and key< l1[j]):
	  l1[j+1]= l1[j]
   	  j -= 1
	l1[j+1] = key
	i+=1
output= l1
# Your code - end
print output
