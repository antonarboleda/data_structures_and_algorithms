# Use this when finding the optimal answer in fixed window size

def sliding_window_fixed(input, window_size):
    # calculate the current window from 0 until window size
    ans = window = input[0:window_size]
    for right in range(window_size, len(input)):
        left = right - window_size
        # remove input[left] from window
        # add window[right] to the window
        # ans = optimal(window, ans)
    return ans
        