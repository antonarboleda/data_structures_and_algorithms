# You are given an integer array cards where cards[i] represents the value of 
# the ith card. A pair of cards are matching if the cards have the same value.

# Return the minimum number of consecutive cards you have to pick up to have a 
# pair of matching cards among the picked cards. If it is impossible to have 
# matching cards, return -1.
"""
Pseudocode
use left and right pointers
if there are 2 or more values at the right pointer, 
   this is valid window so see if it's smaller than previous window size
   decrement in counter map 
otherwise there are no more in window, delete
   move the left pointer forward
otherwise just move right pointer forward

Time: O(N)
Space: O(N)
Start: 7:00am 9/10/23
Finished: 7:51am
Algo: 
- Good, was able to come up with a solution quickly

Impl:
- got stuck with implementation like when to move the left pointer forward
and right pointer forward and what is in the window

Communication:
- Was strong to start bug struggled in debugging

{1:1, 2:1, 5: 1}
res = 2
[1,2,1,5,7] > 3 because we can pick up 3 cards
   l
       r

{1: 2}
[1,1,1] > 2
   l 
     r

[1,2,3]
[5,2,1,5,7]
   l
         r
[5,2,5,5,7]
       r 
   l
[1,2,1,5,7]
     
right = 2
left = 0
{1:1, 2:1}
"""

from typing import List

def minimium_card_pickup(cards: List[int]) -> int:
    result = float("inf")
    counts = {}
    left, right = 0, 0
    while left < len(cards) and right < len(cards):
        if counts.get(cards[right], 0) >= 1:
            result = min(result, right - left + 1)
            counts[cards[left]] -= 1
            left += 1
        else:
            counts[cards[right]] = 1 + counts.get(cards[right], 0)  
            right += 1
    return result if result != float("inf") else -1

assert minimium_card_pickup([1,2,1,5,7]) == 3
assert minimium_card_pickup([1,2,3]) == -1
assert minimium_card_pickup([5,2,5,5,7]) == 2
assert minimium_card_pickup([1,1,1,1,1]) == 2
assert minimium_card_pickup([1,0,3,4,1]) == 5