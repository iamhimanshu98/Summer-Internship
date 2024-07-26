# This program calculates mean, mode and median of an array.

import numpy as np                                  # using numpy library for arrays

def mean(arr,n) :                                   # creating function
    sum = 0
    for i in arr:
        sum+=i                                      # sum of all elements
    return sum/n                                    # returning mean of array

def median(arr,n) :
    if n%2==0:
        return (arr[(n//2)]+arr[(n//2)-1])/2        # when array size is even
    else:
        return arr[(n//2)]                          # when size is odd

def mode(arr,n):
    md = 0                                          # mode variable
    count=0
    for i in arr:
        temp = count                                # temp stores previous maximum frequency of any element
        count=0
        for j in arr:
            if i==j:                                # checking for similar elements in array
                count+=1                            # updating frequency of current element
        
        if temp<count:                              # comparing last frequency
            md = i                                  # update mode value

    return md                                       # returning mode of array

# Main Program

n = int(input("enter size of array: "))             # Size of array/list
ls = []                                             # List to store user inputs
for i in range(n):
    num = int(input("enter element:"))
    ls.append(num)                                  # Adding new element to list

arr = np.array(ls)                                  # List to array using numpy
print("Given array is:",end="")
print(arr)                                          # Input array

print("Mean of array :",round(mean(arr,n),2))       # round() gives only 2 digits after decimal
print("Median of array :",median(arr,n))
print("Mode of array :",mode(arr,n))