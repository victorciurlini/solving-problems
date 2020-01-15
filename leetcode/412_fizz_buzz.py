'''Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.

Example:

n = 15,

Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]'''
import pytest
from typing import List

@pytest.mark.parametrize('input_and_output', [
    (3, [
        "1",
        "2",
        "Fizz",
        ]),
    (5, [
        "1",
        "2",
        "Fizz",
        "4",
        "Buzz"
        ]),
    (15, [
        "1",
        "2",
        "Fizz",
        "4",
        "Buzz",
        "Fizz",
        "7",
        "8",
        "Fizz",
        "Buzz",
        "11",
        "Fizz",
        "13",
        "14",
        "FizzBuzz"
    ])])
def test_fizz_buzz(input_and_output):
    input_number = input_and_output[0]
    expected_output = input_and_output[1]
    predicted_output = fizzBuzz(input_number)
    assert expected_output == predicted_output

def fizzBuzz(n: int) -> List[str]:
    fizz_buzz_list = []
    for i in range(1, n+1):
        word = ""
        if i%3 == 0:
            word += "Fizz"
        if i%5 == 0:
            word += "Buzz"
        if len(word) == 0:
            word = str(i)
        fizz_buzz_list.append(word)
    return fizz_buzz_list
