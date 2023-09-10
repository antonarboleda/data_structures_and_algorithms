# Use this when calculating the longest flexible window
# i.e. find the longest subarray or sequence of numbers

def sliding_window_longest_flexible(input):
    # initialize window, ans
    # left = 0
    for right in range(len(input)):
        # add right to window
        while invalid(window):
            remove input[left] from window
            left += 1
        ans = max(ans, window)
    return ans

# In the shortest flexible window, we find a 
# window valid window and keep shrinking since we know the window
# is valid, we keep shrinking the window and compare it to previous results
# In interviews questions it's usually "Find the minimum in a sequence", "find
# the least number of"
def sliding_window_shortest_flexible(input):
    initialize window, ans
    left = 0
    for right in range(len(input)):
        add right to window
        while valid(window):
            remove input[left] from window
            left += 1
        ans = max(ans, window)
    return ans