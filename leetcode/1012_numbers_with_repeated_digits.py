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

@pytest.mark.parametrize('input_and_output', [(20, 1), (21, 1), (100, 10), (1000, 262), (2000, 758), (738935, 609230)])
def test_num_dup_digits_at_most_n(input_and_output):
    duplicate_count = {}
    input_digit = input_and_output[0]
    expected_output = input_and_output[1]
    predicted_output = numDupDigitsAtMostN(input_digit)

    assert predicted_output == expected_output

def incomplete_fatorial(start_number: int,number_of_loops: int) -> int:
    ''' :Params starting_number, number_of_loops
        :Returns Their incomplete fatorial
    '''
    total_value = 1
    for i in range(0, number_of_loops):
        total_value *= start_number-i
    return total_value
    

def numDupDigitsAtMostN(N: int) -> int:
    ''' :Params Number to count to
        :Returns How many numbers with duplicates there are before the number to count
    '''
    digits = [int(d) for d in str(N)]
    num_digits = len(digits)
    if num_digits < 2:
        return 0
    number_of_non_duplicate_numbers = 0
    for k in range(num_digits - 1):
        number_of_non_duplicate_numbers += 9 * incomplete_fatorial(9, k)
    number_of_non_duplicate_numbers += (digits[0] - 1) * incomplete_fatorial(9, num_digits - 1)
    selected = {digits[0]}
    idx = 1
    for d in digits[1:]:
        idx += 1
        num_choices = d - sum(x < d for x in selected)
        number_of_non_duplicate_numbers += num_choices * incomplete_fatorial(10 - idx, num_digits - idx)
        if d in selected:
            break
        selected.add(d)
    else:
        number_of_non_duplicate_numbers += 1

    return N - number_of_non_duplicate_numbers
