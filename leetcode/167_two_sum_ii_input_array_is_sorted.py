'''
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

Note:

Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.
Example:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
'''
import pytest
from typing import List # Need to import this so we can use List[int] in args
@pytest.mark.parametrize('input_and_output', [(([2,7,11,15], 9), [1,2]), (([2,7,11,15], 18), [2,3])])
def test_num_dup_digits_at_most_n(input_and_output):
    duplicate_count = {}
    input_list = input_and_output[0][0]
    input_target = input_and_output[0][1]
    expected_output = input_and_output[1]
    predicted_output = twoSum(input_list, input_target)

    assert predicted_output == expected_output

def twoSum(numbers: List[int], target: int) -> List[int]:
    return [0,0]
