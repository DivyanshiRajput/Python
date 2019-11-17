def sumDigits(n):
## Your code - begin
    if (n==0):
	return 0
    else:
        return (n%10+ sumDigits(n/10))  
## Your code - end

if __name__ == "__main__":
	n = input("Enter number: ")
	output = sumDigits(n)
	print output
