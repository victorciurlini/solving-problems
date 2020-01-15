'''Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2, 2, 1]
Output: 1
Example 2:

Input: [4, 1, 2, 1, 2]
Output: 4'''
import pytest
from typing import List

@pytest.mark.parametrize('input_and_output', [
    ([2, 2, 1], 1),
    ([4, 1, 2, 1, 2], 4)])
def test_single_number(input_and_output):
    input_list = input_and_output[0]
    expected_output = input_and_output[1]
    predicted_output = singleNumber(input_list)
    assert expected_output == predicted_output


def singleNumber(nums: List[int]) -> int:
    open_set = set()
    closed_set = set()
    for num in nums:
        if num in closed_set:
            continue
        if num in open_set:
            closed_set.add(num)
            open_set.remove(num)
        else:
            open_set.add(num)
    return open_set.pop()
