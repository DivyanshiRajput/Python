def double(l):
## Your code - begin
    return [x*2 for x in l] #using list comprehension for doubling the elements of the list.
## Your code - end
    
if __name__ == "__main__":
  l = [1, 2, 3]
  print "input = ", l
  print double([1, 2, 3])
