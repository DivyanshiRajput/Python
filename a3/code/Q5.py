from Q5input import *

# Your code - begin
sets= [] #this is the expected value for the given value of set1 and set2.
alphabets= "abcdefghijklmnopqrstuvwxyz"
a = list(alphabets)
count=0
for i in set1: #concatenates strings from both the sets 
    for j in set2:
      sets.append(i+j)
      sets[len(sets)-1]=sets[len(sets)-1].lower() #converts string into lower case
output=0
for i in sets:
        count = 0
        for j in range (len(a)): #checks if all the characters are present using ASCII values.
		temp = list(i)
		if (a[j] in temp):
	        	count+=1
	if (count==26):
		output += 1 #increments the number of complete strings

# Your code - end
print sets
print output
