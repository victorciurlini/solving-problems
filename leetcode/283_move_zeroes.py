'''
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
'''
import pytest
from typing import List

@pytest.mark.parametrize('input_and_output', [
    ([0,1,0,3,12], [1,3,12,0,0]),
    ([0,1,0,3,0], [1,3,0,0,0]),
    ([0,0,1], [1,0,0])
    ])
def test_move_zeroes(input_and_output):
    input_list = input_and_output[0]
    expected_output = input_and_output[1]
    moveZeroes(input_list)
    assert expected_output == input_list

def moveZeroes(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    zero_indexes = []
    for i in range(len(nums)):
        if nums[i] == 0:
            nums.append(0)
            zero_indexes.append(i)
    index_decrement = 0
    for index in zero_indexes:
        nums.pop(index + index_decrement)
        index_decrement -= 1
            
