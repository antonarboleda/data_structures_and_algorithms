# Given an integer array nums and an integer k, return true 
# if nums has a good subarray or false otherwise.

# A good subarray is a subarray where:

# its length is at least two, and
# the sum of the elements of the subarray is a multiple of k.
# Note that:

# A subarray is a contiguous part of the array.
# An integer x is a multiple of k if there exists an integer n 
# such that x = n * k. 0 is always a multiple of k.

# [23,2,4,6,7] -> True
#           42 
# k = 4
# cur_sum = 9
# [1,4,5,0,4]
#          r
#        l
# [23,2,4,6,7], k = 6
#       r
#     l
#  cur_sum = 6
# for every number
# add right
# if we've met constraints where we have more than two int and cur_sum >= k
#    check we have a multiple
#    subtract left from sum and advance left
#    
# return False
# sum(subarray) must always be greater than k          
# Start: 12:15PM
# End:  

# [23,2,4,6,11] k = 7
#     l   
#           r
from typing import List

def check_subarray_sum(nums: List[int], k: int) -> bool:
    remainder = {0:-1}
    total = 0
    for i, n in enumerate(nums):
        total += n
        r = total % k
        if r not in remainder:
            remainder[r] = i
        elif i - remainder[r] > 1:
            return True
    return False


assert check_subarray_sum([23,2,4,6,7], 6) == True
assert check_subarray_sum([23,2,6,4,7], 6) == True
assert check_subarray_sum([23,2,4,6,7], 13) == True
print("passed")