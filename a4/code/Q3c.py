def diamond(n,c): #function for printing diamond of height n and character c.
    i=0
    while i<((n/2)+1): #loop for printing upper half of the diamond.
	j = 0
	k = 0
	end = ""
        while j<((n/2)+1-i): #loop for printing spaces.
		end = end + " "
      		j += 1
        while k<(2*i+1): #loop for printing character "c".
               end = end + str(c)
               k += 1
        i += 1
        print end
    i=(n/2)-1
    while i>=0: #loop for printing lower half of the diamond.
	j=(n/2)+1-i
	k=2*i +1
	end= ""
	while j>0: #loop for printing spaces.
		end = end +" "
		j -= 1
	while k>0: #loop for printing character "c".
		end = end + str(c)
		k -= 1
	i -= 1
	print end


