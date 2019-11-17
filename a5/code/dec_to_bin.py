def recurse(ans, n):#recursive function to store the binary conversion in the form of a string.
## Your code - begin
    if (n==0):
	return 0
    elif(n==1):
	return '1'+ans
    if n%2==0:
        ans = "0"+ans
    else:
        ans = "1"+ans
    return recurse (ans, n/2)
## Your code - end
def decToBin(n):#caling function 
  return recurse("", n) #called function

if __name__ == "__main__":
  n = input("Enter number: ")
  output = decToBin(n)
  print output
