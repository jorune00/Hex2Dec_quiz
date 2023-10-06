#!/usr/bin/env python
# jorune00 -- 2023-10-05 20:55:21

import random, sys

def generate_random_hex(length=2):
    """
    Generate a random hex string of length length
    """
    return ''.join([random.choice('0123456789ABCDEF') for x in range(length)])

def end_program():
    """
    End the program
    """
    sys.exit()

def main():
    """
    Main program
    """
    
    while True:
        random_base16_number = generate_random_hex()
        base10_number = int(random_base16_number, 16)
        answer = input(f"What is the decimal value of 0x{random_base16_number}? ")
        if answer == 'q':
            end_program()
        elif int(answer) == base10_number:
            print("Correct!")
        else:
            answer = input("Incorrect. Try again ")

if __name__ == '__main__':
    main()