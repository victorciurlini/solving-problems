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
duplicate_count = {}
@pytest.mark.parametrize('input_and_output', [(20, 1), (21, 1), (100, 10), (1000, 262), (2000, 758), (738935, 609230)])
def test_num_dup_digits_at_most_n(input_and_output):

    input_digit = input_and_output[0]
    expected_output = input_and_output[1]
    predicted_output = numDupDigitsAtMostN(input_digit)

    assert predicted_output == expected_output

@pytest.mark.parametrize('input_and_output', [(1, 9), (2, 90), (3, 738)])
def test_combination_calculate_non_duplicate(input_and_output):

    input_digit = input_and_output[0]
    expected_output = input_and_output[1]
    predicted_output = combination_calculate_non_duplicate(input_digit)

    assert predicted_output == expected_output

def numDupDigitsAtMostN(N: int) -> int:
    number = smart_brute_force(N)
    return number

def has_duplicate(natural_number) -> bool:
    ''' :Params natural number
        :Returns True if input has any repeated digit
                or False if not
    '''
    stringified_natural_number = str(natural_number)
    digits_collected = {}
    for digit in stringified_natural_number:
        if digit in digits_collected:
            return True
        else:
            digits_collected[digit] = 1
    return False

def smart_brute_force(value_to_count: int) -> dict:
    ''' :Params value_to_count as integer
        :Returns list of how many duplicate numbers till the given index
    '''
    stringfied_digits = str(value_to_count)
    number_of_digits = len(stringfied_digits)
    start_number_to_count = 10**(number_of_digits-1) - 1
    start_amount_to_count = start_number_to_count - combination_calculate_non_duplicate( number_of_digits- 1)
    global duplicate_count
    if not start_number_to_count in duplicate_count:
        duplicate_count[start_number_to_count] = start_amount_to_count
    else: 
        start_number_to_count = max(duplicate_count.keys())
        print(start_amount_to_count)
    for i in range(start_number_to_count+1,value_to_count+1):
        if has_duplicate(i):
            duplicate_count[i] = 1 + duplicate_count[i-1]
        else:
            duplicate_count[i] = 0 + duplicate_count[i-1]
    return    duplicate_count[value_to_count]


def combination_calculate_non_duplicate(number_of_digits: int) -> int: 
    ''' :Params The number of digits
        :Returns how many numbers without duplicate digits exists with this number of digits
    '''
    amount_of_duplicate_numbers = 9
    combination_possible = 9
    for i in range(1, number_of_digits):
    # For instance for 2 digits we got 9+9*9
        combination_possible *= (10-i)
        amount_of_duplicate_numbers += combination_possible
    return amount_of_duplicate_numbers

def pre_calculation(value_to_count) -> None:
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

