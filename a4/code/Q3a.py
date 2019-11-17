def diamond(): #function for printing diamond of height 5.
    i=0
    while i<3: #loop for printing upper half of the diamond.
	j = 0
	k = 0
	end = ""
        while j<(3-i): #loop for printing spaces.
		end = end + " "
      		j += 1
        while k<(2*i+1): #loop for printing "*".
               end = end + "*"
               k += 1
        i += 1
        print end
    i=1
    while i>=0: #loop for printing lower half of the diamond.
	j=3-i
	k=2*i +1
	end= ""
	while j>0: #loop for printing spaces.
		end = end +" "
		j -= 1
	while k>0: #loop for printing "*".
		end = end + "*"
		k -= 1
	i -= 1
	print end



