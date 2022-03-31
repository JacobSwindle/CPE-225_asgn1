# Implements operations on binary numbers.
# CSC 225, Assignment 1
# Given code, Spring '22


def add(addend_a, addend_b):
    """
    Add two 16-bit, two's complement numbers; ignore carries/overflows.
    TODO: Implement this function. Do *not* convert the numbers to decimal.

    :param addend_a: A bitstring representing the first number
    :param addend_b: A bitstring representing the second number
    :return: A bitstring representing the sum
    """
    result = ''
    carry = 0
    for i in range(15, -1, -1):
        bit_a = addend_a[i]
        bit_b = addend_b[i]
        one_count = 0
        next = -1

        if (bit_a == '1'):
            one_count += 1
        if (bit_b == '1'):
            one_count += 1
        if (carry == 1):
            one_count += 1
        
        if (one_count == 0):
            carry = 0 ##
            next = '0'
        elif (one_count == 1):
            carry = 0
            next = '1'
        elif (one_count == 2):
            carry = 1
            next = '0'
        else:
            carry = 1
            next = '1'
        
        result = next + result
    
    return result


def negate(number):
    """
    Negate a 16-bit, two's complement number.
    TODO: Implement this function. Do *not* convert the number to decimal.

    :param number: A bitstring representing the number to negate
    :return: A bistring representing the negated number
    """

    result = ''
    for i in range(16):
        if number[i] == '1':
            result += '0'
        else:
            result += '1'
    
    one = '0000000000000001'
    return add(result, one)


def subtract(minuend, subtrahend):
    """
    Subtract one 16-bit, two's complement number from another.
    TODO: Implement this function. Do *not* convert the numbers to decimal.

    :param minuend: A bitstring representing the number from which to subtract
    :param subtrahend: A bitstring representing the number to subtract
    :return: A bitstring representing the difference
    """
    negatron = negate(subtrahend)
    return add(minuend, negatron)


def multiply(multiplicand_a, multiplicand_b):
    """
    Multiply two 16-bit, two's complement numbers; ignore carries/overflows.
    TODO: Implement this function. Do *not* convert the numbers to decimal.

    :param multiplicand_a: A bitstring representing the first number
    :param multiplicand_b: A bitstring representing the second number
    :return: A bitstring representing the product
    """
    negative_count = 0
    if (multiplicand_a[0] == '1'):
        multiplicand_a = negate(multiplicand_a)
        negative_count += 1
    if (multiplicand_b[0] == '1'):
        multiplicand_b = negate(multiplicand_b)
        negative_count += 1
    
    result = '0000000000000000'
    mults_from_one_digit = []
    for i in range(16):
        if (multiplicand_a[15-i] == '1'):
            one_digit_product = multiplicand_b[i:] + '0'*i
            mults_from_one_digit.append(one_digit_product)

    for i in range(len(mults_from_one_digit)):
        result = add(result, mults_from_one_digit[i])
    
    if (negative_count == 1):
        result = negate(result)
    return result



def binary_to_decimal(number):
    """
    Convert a 16-bit, two's complement number to decimal.
    TODO: Implement this function.

    :param number: A bitstring representing the number to convert
    :return: An integer, the converted number
    """
    total = 0
    for i in range(len(number)-1, -1, -1):
        if (number[i] == '1'):
            total += 2 ** (15-i)
    
    return total


def decimal_to_binary(number):
    """
    Convert a decimal number to 16-bit, two's complement binary.
    TODO: Implement this function.

    :param number: An integer, the number to convert
    :return: A bitstring representing the converted number
    :raise OverflowError: If the number cannot be represented with 8 bits
    """
    if (number > 255 or number < -256):
        raise OverflowError
    
    result = '0000000000000000'
    for i in range(number):
        result = add(result, '0000000000000001') # :)
    
    return result

