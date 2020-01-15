'''
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
'''
import pytest

@pytest.mark.parametrize('input_and_output', [
    (["anagram", "nagaram"], True),
    (["rat", "car"], False),
    (["ab", "a"], False)
    ])
def test_is_anagram(input_and_output):
    s_input_string = input_and_output[0][0]
    t_input_string = input_and_output[0][1]
    expected_output = input_and_output[1]
    predicted_output = isAnagram(s_input_string, t_input_string)
    assert expected_output == predicted_output


def isAnagram(s: str, t: str) -> bool:
    letters_count = dict()
    for character in s:
        if character in letters_count:
            letters_count[character] += 1
        else:
            letters_count[character] = 1
    for character in t:
        if character in letters_count:
            letters_count[character] -= 1
            if letters_count[character] < 0:
                del letters_count[character]
        else:
            return False
    return True
