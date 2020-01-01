'''
Given an array nums of n integers and an integer target, 
find three integers in nums such that the sum is closest to target. Return the sum of the three integers.
You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
'''
import pytest
from typing import List # Need to import this so we can use List[int] in args
from math import log10
@pytest.mark.parametrize('input_and_output', [(([-1, 2, 1, -4], 1), 2), (([2,7,11,15], 21), 20)])
def test_num_dup_digits_at_most_n(input_and_output):
    duplicate_count = {}
    input_list = input_and_output[0][0]
    input_target = input_and_output[0][1]
    expected_output = input_and_output[1]
    predicted_output = threeSumClosest(input_list, input_target)

    assert predicted_output == expected_output


def threeSumClosest(nums: List[int], target: int) -> int:
  return target