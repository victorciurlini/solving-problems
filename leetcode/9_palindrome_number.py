'''
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
'''
import pytest

@pytest.mark.parametrize('input_and_output', [(121, True), (-121, False)])
def test_palindrome_number(input_and_output):
  input_integer = input_and_output[0]
  expected_output = input_and_output[1]
  predicted_output =  isPalindrome(input_integer)
  assert expected_output == predicted_output


def isPalindrome(x: int) -> bool:
  return  False