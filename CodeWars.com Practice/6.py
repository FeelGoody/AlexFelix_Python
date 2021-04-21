# https://www.codewars.com/kata/526571aae218b8ee490006f4/train/python
# Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary representation of that number. You can guarantee that input is non-negative.

# Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case
def count_bits(n):
    print("The number of bits requres to store your number is:  ", (n.bit_length()))
    print("The binary number your number is:  ", str(bin(n)).replace('0b',''))
    return 0

count_bits(int(input("Plese enter any positive numer:  ")))
print()
