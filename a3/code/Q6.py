from Q6input import *

# Your code - begin
dict={}
char={}
count=0
l= len(inp)
for i in range (l):# stores the character as keys with its count as values
    for j in range (l):
      if (inp[i]==inp[j]):
        count +=1
    dict[inp[i]]= count
    count= 0
for x in dict:# stores the count as key with its value as a list of characters with the same count
    if dict[x] not in char:
	char[dict[x]]=[]
	char[dict[x]].append(x)
    else:
	char[dict[x]].append(x)
count=[]
count= [x for x in char.keys()]# stores the keys of char
count.sort()# sorts count
nfreq=char[count[len(count)-N]# nfreq stores a list containing all characters with Nth most frequency
nfreq.sort()# sorts the characters by ASCII value
output=nfreq[0]  

# This is the expected output for the given input.

# Your code - end
print output
