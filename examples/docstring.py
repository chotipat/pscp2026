"""
This module provides a high-level summary of the program's functionality.
It can contain multiple classes and functions, though classes may not be
covered in this course.

During the first few weeks, you may only need to write a single function.
"""


def check_ssn(ssn):
    """Return 'yes' if ssn has 13 digits, 'no' otherwise."""
    if len(ssn) == 13:
        return "yes"
    return "no"


def main():
    """Print result from check_ssn function"""
    ssn = input()
    print(check_ssn(ssn))


main()
