# Binary to Decimal #

import math

while True:
    binary = input('Type a binary string with lenght between 1 to 8 characters: ')

    binary.split()

    isBinary = False

    for i in range(len(binary)):
        if binary[i] == '1' or binary[i] == '0':
            isBinary = True
        else:
            isBinary = False
            print('You can just type 0 or 1')
            break

    if isBinary == True:
        decimal = 0
        for i in range(len(binary)):
            decimal += int(binary[i]) * pow(2, int(len(binary)) - i - 1)

        print(f'Your binary number is: {decimal}')

    else:
        continue