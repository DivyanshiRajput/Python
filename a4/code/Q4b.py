def ndiamond(n): #function to print a numerical diamond of height n.
	i=0
	a= (n+1)/2
	while (i<a): #loop for printing the upper half of the diamond.
		j=0
        	k=0
        	end= ""
        	while (j<a-i): #loop for spaces.
        	    end = end + " "
        	    j += 1
        	while (k<(i+1)): #printing numbers in increasing order.
        	    end = end + str(k+1)
        	    k += 1
		k -= 1
		while (k>0): #printing numbers in decreasing order.
		    end = end + str(k)
		    k -= 1
		print end
		i += 1
	i -= 2
	while (i>=0): #loop for printing the lower half of the diamond.
		j=0
		k=0
		end = ""
		while (j<a-i): #loop for spaces.
			end = end + " "
			j += 1
		while (k<(i+1)): #loop for printing numbers in increasing order.
			end = end + str(k+1)
			k += 1
		k -= 1
		while (k>0): #loop for printing numbers in decreasing order.
			end = end + str(k)
			k -= 1
		print end
		i -= 1

