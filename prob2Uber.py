# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 13:22:58 2019

This problem was asked by Uber.

Given an array of integers, 
return a new array such that each element at index i of 
the new array is the product of all the numbers in the original array 
except the one at i.

For example, if our input was 
[1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. 
If our input was [3, 2, 1], the expected output would be [2, 3, 6]

@author: murph
"""
def productArray(arr, n): 
    # Allocate memory for the product array  
    prod = [1 for i in range(n)] 

    # Base case 
    if n == 1: 
        return arr[0]
    
    else:
        i, temp = 1, 1
          
        # In this loop, temp variable contains product of 
        # elements on left side excluding arr[i]  
        for i in range(n):
            prod[i] = temp 
            temp *= arr[i]

        # Initialize temp to 1 for product on right side  
        temp = 1
          
        # In this loop, temp variable contains product of 
        # elements on right side excluding arr[i]  
        # backwards from the last item
        for i in range(n - 1, -1, -1): 
            prod[i] *= temp 
            temp *= arr[i]

        # Print the constructed prod array  
        return prod
  
# Driver Code 
arr = [1, 2, 3, 4, 5] 
n = len(arr) 
print(productArray(arr, n))
