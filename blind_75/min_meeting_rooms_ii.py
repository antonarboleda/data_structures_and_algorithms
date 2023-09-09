# Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.


# Example 1:

# Input: intervals = [[0,30],[5,10],[15,20]]
# Output: 2
# Example 2:

# Input: intervals = [[7,10],[2,4]]
# Output: 1
# 9/8/23
# Grade - C - no pass
# start time: 11:10am
# finished at: 11:53


"""
meeting_rooms = 2
start: 0
end:0 
[[2,5],[3,4],[7,10],[8, 11]]
end_times = heap([5, 7])
start >= end - we don't need a new meeting room 
can we re-use the meeting room?
sort by start times
[[0,30],[5,10],[15,20]]
heap = heap([15, 30]) -> 2
[0,20] [20,30]
heap([])

pseudocode
use a min-heap called end_times so we know if a meeting room will be available 
as we go through each meeting
  2 cases
  - we need another room - the start time < end_times[0]
    add to the end_times heap, we need another room
  - use an existing room - start time >= earliest end time
    heappushpop endtimes heap, we can re-use the room with the earliest 
    end time

[[2,5],[3,4],[7,10],[8, 11]]
                 i
end_times = [10,11]

N Log N
"""
from typing import List
from heapq import heapify, heappush, heappushpop

def meeting_rooms(intervals: List[List[int]]):
    intervals.sort(key=lambda x: x[0])
    end_times = [intervals[0][1]]
    heapify(end_times)
    
    num_rooms = 0
    for i in range(1,len(intervals)):
        start, end = intervals[i]
        if start >= end_times[0]:
            heappushpop(end_times, end) 
        else:
            heappush(end_times, end)
        num_rooms = max(num_rooms, len(end_times))
    return num_rooms



assert meeting_rooms([[2,5],[3,4],[7,10],[8, 11]]) == 2
assert meeting_rooms([[7,10],[2,4]]) == 1
assert meeting_rooms([[5,8],[6,8]]) == 2
assert meeting_rooms([[1,5],[8,9],[8,9]]) == 2


print("tests passed!")



- Requirements 5 mins
    - Functional [5 reqs]
    - Non Functional [3 reqs]
- Apis/ Requests/ Data Models[7 mins]
    - Don’t forget your protocols in the API conversation.
    - Don’t forget the API methods,
    - Talk about traffic considerations by endpoint, stratify endpoints by traffic and data type. If we supported live streams for instance, web hooks would be better compared to https.
- Estimates [5mins, Generate Read/ Write Throughput]
- Schemas [5 mins]
- High Level Design [7 mins]
- Deep Dive [15-20 mins]