def recurse(n,i):
## Your code - begin
    l= len(n)
    if (i<(l/2)):
        if (n[i]==n[l-i-1]):#comparing i'th element from the start and end.
            return recurse(n,i+1)#recursive function for comparing whole string.
        else:
            return False
    return True
## Your code - end

def isPalindrome(n):#calling function.
  return recurse(n,0)#called function.
  
if __name__ == '__main__':
	n = raw_input("Enter string: ")
	output = isPalindrome(n)
	print output
