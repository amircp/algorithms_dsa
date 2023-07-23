"""
    Practicing String Manipulation
    Convert roman numbers to integers
"""


ROMANS = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

def calculate_roman_number(roman_number: str) -> int:

    result = 0
    n = len(roman_number)

    for i in reversed(range(n - 1)):

        current = ROMANS[roman_number[i]]
        next_value = ROMANS[roman_number[i + 1]]

        if current < next_value:
            result -= current
        else:
            result += current

    last_digit = ROMANS[roman_number[-1]]
    result += last_digit

    return result

print(calculate_roman_number("XIV"))

