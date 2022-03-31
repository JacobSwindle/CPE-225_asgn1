# Implements operations on hexadecimal numbers.
# CSC 225, Assignment 1
# Given code, Winter '20

hex_translation_guide = [
    ['0000', '0'],
    ['0001', '1'],
    ['0010', '2'],
    ['0011', '3'],
    ['0100', '4'],
    ['0101', '5'],
    ['0110', '6'],
    ['0111', '7'],
    ['1000', '8'],
    ['1001', '9'],
    ['1010', 'A'],
    ['1011', 'B'],
    ['1100', 'C'],
    ['1101', 'D'],
    ['1110', 'E'],
    ['1111', 'F']
]

def binary_to_hex(number):
    """
    Convert a 16-bit binary number to hexadecimal.
    TODO: Implement this function. Do *not* convert the number to decimal.

    :param number: A bitstring representing the number to convert
    :return: A hexadecimal string, the converted number
    """
    hs = [number[:4], number[4:8], number[8:12], number[12:]]
    result = '0x'

    for h in hs:
        for digit in hex_translation_guide:
            if h == digit[0]:
                result += digit[1]
                break

    return result


def hex_to_binary(number):
    """
    Convert a hexadecimal number to 16-bit binary.
    TODO: Implement this function. Do *not* convert the number to decimal.

    :param number: A hexadecimal string, the number to convert
    :return: A bitstring representing the converted number
    """
    real = number[2:]
    result = ''

    for char in real:
        for digit in hex_translation_guide:
            if char == digit[1]:
                result += digit[0]
                break
    
    return result














'''

for h in hs:
        if h == '0000':
            result += '0'
        elif h == '0001':
            result += '1'
        elif h == '0010':
            result += '2'
        elif h == '0011':
            result += '3'
        elif h == '0100':
            result += '4'
        elif h == '0101':
            result += '5'
        elif h == '0110':
            result += '6'
        elif h == '0111':
            result += '7'
        elif h == '1000':
            result += '8'
        elif h == '1001':
            result += '9'
        elif h == '1010':
            result += 'A'
        elif h == '1011':
            result += 'B'
        elif h == '1100':
            result += 'C'
        elif h == '1101':
            result += 'D'
        elif h == '1110':
            result += 'E'
        else:
            result += 'F'


'''