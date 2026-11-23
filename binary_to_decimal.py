#binary_to_decimal.py - convert a binary number to decimal

binary = input("Enter a binary number: ")

decimal = 0
for digit in binary:
    decimal = decimal * 2 + int(digit)

print(f"{binary} in binary = {decimal} in decimal")