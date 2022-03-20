# Binary to Decimal #

import math

binary = input('Type a binary string with lenght between 1 to 8 characters:\n')

decimal = 0

for i in range(len(binary)):
    decimal += int(binary[i]) * pow(2, int(len(binary)) - i - 1)

print(f'Your binary number is: {decimal}')
