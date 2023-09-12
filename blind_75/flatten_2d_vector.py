# # https://leetcode.com/problems/flatten-2d-vector/

# Design an iterator to flatten a 2D vector. It should support the next and 
# hasNext operations.

# Implement the Vector2D class:

# Vector2D(int[][] vec) initializes the object with the 2D vector vec.
# next() returns the next element from the 2D vector and moves the pointer one 
# step forward. You may assume that all the calls to next are valid.
# hasNext() returns true if there are still some elements in the vector, and 
# false otherwise.

# Start: 9:58AM
# Finish: 10:25AM
# Grade: Optimal solution in 27 minutes. Good problem solving in under 30 min

"""
initialize a pointer at first list
i is the pointer for the inner list, j is outer list
while i is an invalid index
  increment j
  i = 0

we now know that i is a valid index this is the value to yield
save it
increment i
yield
move j
[
  [
    [],[],[1,2],[],[3],[4]
  ]                   i
                        j     
]
"""
from typing import List

class Vector2D:
    def __init__(self, vec: List[List[int]]):
        self.i = 0 # inner
        self.j = 0 # outer
        self.vec = vec

    def next(self) -> int:
        # invalid indexing for i
        while self.i >= len(self.vec[self.j]):
            self.j += 1
            self.i = 0
        
        # valid index
        val = self.vec[self.j][self.i]
        self.i += 1
        yield val

    def hasNext(self) -> bool:
        while self.j < len(self.vec)and self.i >= len(self.vec[self.j]):
            self.j += 1
            self.i = 0
        
        return self.j < len(self.vec) and self.i < len(self.vec[self.j])

v = Vector2D([[1, 2], [3], [4]])
assert next(v.next()) == 1
assert next(v.next()) == 2
assert next(v.next()) == 3
assert v.hasNext() == True
assert v.hasNext() == True
assert next(v.next()) == 4
assert v.hasNext() == False
assert v.hasNext() == False
         