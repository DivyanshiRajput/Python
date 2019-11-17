from Q3input import *

# Your code - begin
inp= inp.lower
alphabets= "abcdefghijklmnopqrstuvwxyz"
dict={}
count=0
l= len(inp)
for i in range (l):
  if inp[i] in alphabets: # takes only lowercase alphabets into consideration
    for j in range (l): 
      if (inp[i]==inp[j]):
        count +=1          # increments count if an alphabet is found in the input string
    dict[inp[i]]= count   # updates a dictionary 
    count= 0
for x in dict:
  if (dict[x] !=1):# if count is not 1, then output will be False, else true
    output= "false"
  else:
    output= "true"

# Your code - end
print output

