'''
Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.

'''

nums = [1, 2, 0]
i = 0
#-1 0 1 3 4
#0 1 2
#0 2 3 4
while i < len(nums) - 1:
    nums.sort()
    # if the number we are looking for is between two numbers
    if nums[i+1] - nums[i] != 1 and nums[i+1] > 0:
        print(nums[i+1] - nums[i])
        break
    #if the num is above nums[i+1]
    elif nums[i+1] - nums[i] == 1 and nums[i+1] > 1:
        print(nums[i+1] + 1)
        break
    i += 1


''' 
def findPos(numL):
    nums.sort()
    # if the number we are looking for is between two numbers
    if nums[i+1] - nums[i] != 1 and nums[i+1] > 0:
        print(nums[i+1] - nums[i])
        break
    #if the num is above nums[i+1]
    elif nums[i+1] - nums[i] == 1 and nums[i+1] > 1:
        print(nums[i+1] + 1)
        break
    i += 1
findPos(numL)
'''
