# Array printing utility function. Feel free to use.
def printArr(arr, k): #fuction for printing array. 
  for i in range(k): #loop for printing elements of array.
    print(str(arr[i]) + " "), 
  print
  
def printSeqUtil(n, k, len1, arr): #recursive function to declare the array.
## Your code - begin
    if (len1 == k): #condition for when array should be printed.
        printArr(arr, k); 
        return;
    if(len1==0):#assigning the value of i which will be appended in the array.
        i=1
    else:
        i=arr[len1-1]+1#assigning the value of i which will be appended in the array.
    len1+=1 #incrementing value of length.
    while (i<=n):#loop for printing all arrays for the given index.
        arr[len1-1]=i
        printSeqUtil(n,k,len1,arr)#calling function for appending the next element in the array. 
        i+=1 #incrementing value of i
    len1-=1 #restoring value of length for the next set of arrays.
## Your code - end
  
def printSeq(n, k):#calling function. 
    arr = [0] * k  
    len1 = 0
    printSeqUtil(n, k, len1, arr) #called function.

if __name__ == "__main__":
  n = input("Enter n: ")
  k = input("Enter k: ")
  printSeq(n, k)
