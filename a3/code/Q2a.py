from Q2input import *

# Your code - begin
for key in Dic2:
   if key in Dic1:
      Dic1[key] = Dic2[key] +Dic1[key] #adds values of common keys
   else:
      Dic1.update({key : Dic2[key]})#adds new keys into dictionary 

output = Dic1 # should be {'some':20, 'fuzzy':25, 'data':17, 'logic':0. 'marks':100} for the given input.

# Your code - end
print output
