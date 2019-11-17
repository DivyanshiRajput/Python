from Q6input import *

# Your code - begin
i=1
while (i<len(l)):
	j= i-1
	key= l[i]
	while (j>=0 and key< l[j]):
	  l[j+1]= l[j]
   	  j -= 1
	l[j+1] = key
	i+=1

if (len(l)%2==0):
	key= len(l)/2
	output= float(l[key] + l[key+1])/2
else:
    key=((len(l)+1)/2)
    output= l[key]


# Your code - end
print output
