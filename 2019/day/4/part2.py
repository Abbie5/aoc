#!/usr/bin/env python3

def has_two_adjacent(password):
    """Check if the password contains a pair of adjacent digits"""
    last_char = None
    num_adjacent = 0

    for char in password:
        if char == last_char:
            num_adjacent += 1
        else:
            if num_adjacent == 1:
                return True

            last_char = char
            num_adjacent = 0

    if num_adjacent == 1:
        return True
    else:
        return False


def digits_never_decrease(password):
    """Check if the digits never decrease going from left to right"""
    last_digit = None

    for char in password:
        digit = int(char)
        if (last_digit == None) or (digit >= last_digit):
            last_digit = digit
        else:
            return False

    return True

def is_valid(password):
    """Check if password meets all conditions"""
    return has_two_adjacent(password) and digits_never_decrease(password)

min, max = 387638, 919123

num_valid_passwords = 0
for password in range(min, max+1):
    if is_valid(str(password)):
        num_valid_passwords += 1

print(num_valid_passwords)
