from Q2input import *

# Your code - begin
output = inp
stack=[]
opening= ['(','[','{']
closing= [')',']','}']
pairs= ['()','[]','{}']
i=0
while i<len(inp):
	x=inp[i]
	l=len(stack)
	if x in opening:
	    stack.append(x)
	elif x in closing:
	    if (len(stack)!=0 and (stack[l-1]+x) in pairs):
		stack.pop()
	    else:
		output="unbalanced"
		break
	i+=1
if len(stack)==0:
	output= "true"
else:
	output= "false"
# Your code - end
print output
