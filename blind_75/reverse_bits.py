# Reverse bits of a given 32 bits unsigned integer.
"""
3 > 00000001 -> 
    00000001

Idea 1

- convert int to binary string
    % by 2 to get last 1 digit
- reverse string
- convert binary string back to integer
Time: O(N) 
Space: O(N)

Idea 2

Psuedocode
Mod by 2 to get the right most bit 
right shift n by 1
add modded value to result int
left shift result int

Do all of above 32 times for a 32 bit int. 
Time: O N
Space: O 1 

n = 0000 0000   
result = 01 0100

Start Time: Around 8:30am
Finish Time around 9:am
Grade: B

My psuedocode was off which cause some test cases to fail. I initially said 
add the remainder of modded value, 1 or 0 to the result and then right shift, 
but we need to left shift the result before adding anything to it. This is 
so that the 0th bit is always zero before we add the modded value to the result.
"""
def reverseBits(n: int) -> int:
    result = 0
    for _ in range(32):
        modded_val = n % 2
        result = result << 1
        result += modded_val
        n = n >> 1
    return result

assert reverseBits(1) == 256
assert reverseBits(2) == 128
print("test passed")
