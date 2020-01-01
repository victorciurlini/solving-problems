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


def threeSumClosest(numbers: List[int], target: int) -> int:
    closest_distance = float('inf')
    closest_number = None
    numbers.sort()
    numbers_size = len(numbers)
    for anchor_index, anchor_number in enumerate(numbers[0:-2]):
        if anchor_index > 0 and numbers[anchor_index-1] == anchor_number: continue
        bottom_index, top_index = anchor_index+1, numbers_size-1

        summation = anchor_number + numbers[bottom_index] + numbers[bottom_index+1]
        if summation > target and abs(summation - target) < closest_distance:
            closest_distance = abs(summation - target)
            closest_number = summation
        else:
            summation = anchor_number + numbers[top_index] + numbers[top_index-1]
            if summation < target and abs(summation - target) < closest_distance:
                closest_distance = abs(summation - target)
                closest_number = summation
            else:
                while(bottom_index < top_index):
                    summation = anchor_number + numbers[bottom_index] + numbers[top_index]
                    if abs(summation - target) < closest_distance:
                        closest_distance = abs(summation - target)
                        closest_number = summation
                    if summation > target:
                        top_index -= 1
                    elif summation < target:
                        bottom_index += 1
                    else: 
                        return closest_number
    return closest_number