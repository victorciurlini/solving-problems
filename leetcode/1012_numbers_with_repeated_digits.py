'''
Given a positive integer N, return the number of positive integers less than or equal to N that have at least 1 repeated digit.

 

Example 1:numDupDigitsAtMostN

Input: 20
Output: 1
Explanation: The only positive number (<= 20) with at least 1 repeated digit is 11.
Example 2:

Input: 100
Output: 10
Explanation: The positive numbers (<= 100) with atleast 1 repeated digit are 11, 22, 33, 44, 55, 66, 77, 88, 99, and 100.
Example 3:

Input: 1000
Output: 262
 

Note:

1 <= N <= 10^9
'''
import pytest

@pytest.mark.parametrize('input_and_output', [(20, 1), (100, 10), (1000, 262), (2000, 758), (738935, 609230)])
def test_num_dup_digits_at_most_n(input_and_output):
  input_digit = input_and_output[0]
  expected_output = input_and_output[1]
  predicted_output = numDupDigitsAtMostN(input_digit)

  assert predicted_output == expected_output


def numDupDigitsAtMostN(N: int) -> int:
    list_counting = pre_calculation(N)
    return list_counting[N]

def has_duplicate(natural_number) -> bool:
    ''' :Params natural number
        :Returns True if input has any repeated digit
                or False if not
    '''
    if natural_number < 10:
        return False
    digits_in_number = {}
    while(natural_number > 0):
        n = natural_number%10
        if n in digits_in_number:
            return True
        else:
            digits_in_number[n] = 1
        natural_number = natural_number//10
    return False

def pre_calculation(value_to_count) -> list:
    ''' :Params value_to_count as integer
        :Returns list of how many duplicate numbers till the given index
    '''
    global duplicate_count
    duplicate_count = []
    duplicate_count.append(0)
    for i in range(1, value_to_count+1):
        if has_duplicate(i):
            duplicate_count.append( 1 + duplicate_count[i-1])
        else:
            duplicate_count.append( 0 + duplicate_count[i-1])
    