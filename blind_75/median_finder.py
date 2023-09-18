# https://leetcode.com/problems/find-median-from-data-stream/
# Find Median from Data Stream

# The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

"""
Idea ----------

1 heap to keep track of the largest numbers
1 heap to keep track of the smallest numbers

findMedian 
 2 cases
 1. if they're equal size - get average
 2. if they're not equal size, then take the max of the smaller numbers

 addNum
if n >= min of larger numbers or there is nothing in larger numbers, insert there
    insert into larger
    if larger has more chars
    rebalance
otherwise insert in smaller pile
    if len(smaller_pile) > len(larger_pile):
       rebalance
    insert into smaller pile

 
   12 45

1
     min_heap 
1. 7 add 1
2. 1 add 7
3. 12 34 add 5
4. 12345 add 0
smaller_numbers = [-7]  
----------------- Post practice session notes

Started at 4:14 pm
Finished after 40 minutes having to use the compiler to point out some failed 
test cases. Additionally, I fumbled during the middle of implementation when 
trying to always balance the min and max heaps so that their sizes were always 
correct - where both were the same size or their lengths differed by 1. 
I looked at some answers online and realized that using heappushpop with an 
element will always return the smallest element. 
That's what the optimized solution is. In an interview those 10 minutes or so 
would have cost me from being a strong yes.

I think the main take away here is to have a better understanding of a min heap 
vs max heap through repetition. I had to 
recall if in python the heapify methods were for a min heap or maxheap.
"""
from heapq import heappush, heappop, heappushpop, heapify

class MedianFinder:

    def __init__(self):
        self.smaller_numbers = [] # max heap
        self.larger_numbers = [] # min heap

    def addNum(self, num: int) -> None:
        if not self.smaller_numbers and not self.larger_numbers:
            heappush(self.smaller_numbers, -num)
            return
        
        if self.larger_numbers and num > self.larger_numbers[0]:
            heappush(self.larger_numbers, num)
        else:
            heappush(self.smaller_numbers, -num)
        
        if len(self.larger_numbers) > len(self.smaller_numbers):
            val = heappop(self.larger_numbers)
            heappush(self.smaller_numbers, - val)

        if len(self.smaller_numbers) - len(self.larger_numbers) == 2:
            val = heappop(self.smaller_numbers)
            heappush(self.larger_numbers, -val)
        



    def findMedian(self) -> float:
        if not self.larger_numbers:
           return -self.smaller_numbers[0]

        if len(self.smaller_numbers) == len(self.larger_numbers):
           return (-self.smaller_numbers[0] + self.larger_numbers[0]) / 2
        
        return -self.smaller_numbers[0] 

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()