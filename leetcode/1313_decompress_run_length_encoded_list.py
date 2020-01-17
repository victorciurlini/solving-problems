'''
We are given a list nums of integers representing a list compressed with run-length encoding.

Consider each adjacent pair of elements [a, b] = [nums[2*i], nums[2*i+1]] (with i >= 0).  For each such pair, there are a elements with value b in the decompressed list.

Return the decompressed list.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [2,4,4,4]
Explanation: The first pair [1,2] means we have freq = 1 and val = 2 so we generate the array [2].
The second pair [3,4] means we have freq = 3 and val = 4 so we generate [4,4,4].
At the end the concatenation [2] + [4,4,4,4] is [2,4,4,4].

'''

import pytest
from typing import List # Need to import this so we can use List[int] in args
from math import log10
@pytest.mark.parametrize('input_and_output', [([1,2,3,4], [2,4,4,4])])
def test_decompressRLElist(input_and_output):
    input_digit = input_and_output[0]
    expected_output = input_and_output[1]
    predicted_output = decompressRLElist(input_digit)
    assert predicted_output == expected_output


def decompressRLElist(nums: List[int]) -> List[int]:
    res = []        
    for i in range(0, len(nums), 2):
        res.extend([nums[i + 1]] * nums[i])
    return res