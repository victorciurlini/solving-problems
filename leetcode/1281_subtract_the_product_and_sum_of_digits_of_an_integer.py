'''
Given an integer number n, return the difference between the product of its digits and the sum of its digits.
 

Example 1:

Input: n = 234
Output: 15 
Explanation: 
Product of digits = 2 * 3 * 4 = 24 
Sum of digits = 2 + 3 + 4 = 9 
Result = 24 - 9 = 15
Example 2:

Input: n = 4421
Output: 21
Explanation: 
Product of digits = 4 * 4 * 2 * 1 = 32 
Sum of digits = 4 + 4 + 2 + 1 = 11 
Result = 32 - 11 = 21
'''
import pytest

@pytest.mark.parametrize('input_and_output_integers', [(234, 15), (4421, 21)])
def testSPS(input_and_output_integers):
  input_integer = input_and_output_integers[0]
  correct_output_integer = input_and_output_integers[1]
  predicted_output_integer = subtractProductAndSum(input_integer)

  assert correct_output_integer == predicted_output_integer


def subtractProductAndSum( n: int) -> int:
  return n
