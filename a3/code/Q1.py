from Q1input import *

# Your code - begin
dict={}
count=0
l= len(inp)
for i in range (l): 
   for j in range (l):
      if (inp[i]==inp[j]):
        count +=1  #if two numbers are equal in input, increases count by one
   dict[inp[i]]= count #adds key value and count to the dictionary
   count= 0
		 
output = dict  
# This is the answer for the given input.
# Your code - end

print output
