'''
Given a text file file.txt that contains list of phone numbers (one per line), write a one liner bash script to print all valid phone numbers.

You may assume that a valid phone number must appear in one of the following two formats: (xxx) xxx-xxxx or xxx-xxx-xxxx. (x means a digit)

You may also assume each line in the text file must not contain leading or trailing white spaces.

Example:

Assume that file.txt has the following content:

987-123-4567
123 456 7890
(123) 456-7890
Your script should output the following valid phone numbers:

987-123-4567
(123) 456-7890
'''
import pytest
from unittest import mock


@pytest.mark.parametrize('input_and_output', [
    ('987-123-4567\n123 456 7890\n(123) 456-7890',
        '987-123-4567\n(123) 456-7890\n')])
def test_check_possibility(capsys, input_and_output):
    mocked_text_content = input_and_output[0]
    expected_output = input_and_output[1]
    mocked_open_function = mock.mock_open(read_data=mocked_text_content)

    with mock.patch("builtins.open", mocked_open_function):
        with open("any_string") as f:
            print(f.read())
    readAndPrintPhoneNumbers()
    captured_output = capsys.readouterr().out
    assert captured_output == expected_output


def readAndPrintPhoneNumbers(text_file='file.txt') -> None:
    with mock.patch("builtins.open", mocked_open_function):
        with open("any_string") as f:
                print(f.read())