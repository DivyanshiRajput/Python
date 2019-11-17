from Q4input import *

# Your code - begin
output=[] # should be [1,2,5,7,0,0] for the given input.
output=[notzero for notzero in inp if notzero!=0] #add nonzero digits into the list
output.extend([zero for zero in inp if zero==0]) #append the zeroes to the output list

# Your code - end
print output
