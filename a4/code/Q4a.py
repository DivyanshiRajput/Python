def ndiamond(): #function to print a numerical diamond of height 5.
	i=0
	while (i<3): #loop to print the first 3 lines of the diamond.
		j=0
        	k=0
        	end= ""
        	while (j<3-i): #loop for spaces.
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
		i += 1
	i=1
	while (i>=0): #loop to print the last 2 lines of the numerical diamond.
		j=0
		k=0
		end = ""
		while (j<3-i): #loop for spaces.
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

