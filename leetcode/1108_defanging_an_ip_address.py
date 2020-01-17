
'''
Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".


Example 1:

Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"

Example 2:

Input: address = "255.100.50.0"
Output: "255[.]100[.]50[.]0"

'''

import pytest
from typing import List # Need to import this so we can use List[int] in args
from math import log10
@pytest.mark.parametrize('input_and_output', [("1.1.1.1", "1[.]1[.]1[.]1"), ("255.100.50.0", "255[.]100[.]50[.]0")])
def test_defangIPaddr(input_and_output):
    input_digit = input_and_output[0]
    expected_output = input_and_output[1]
    predicted_output = defangIPaddr(input_digit)
    assert predicted_output == expected_output


    def defangIPaddr(address: str) -> str:
        return address.replace(".", "[.]")