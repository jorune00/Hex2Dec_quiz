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
        correct_base10_number = int(random_base16_number, 16)
        is_correct = False
        
        while not is_correct:
            try:
                answer = input(f"What is the decimal value of 0x{random_base16_number}? ")
                if answer.lower() == 'q':
                    end_program()
                
                answer = int(answer)
                if answer == correct_base10_number:
                    print("Correct!")
                    is_correct = True
                    continue  # go to next iteration
                else:
                    print("Incorrect. Try again or press 'q' to quit.")
            except ValueError:
                print("Invalid input. Please enter a number or 'q' to quit.")

if __name__ == '__main__':
    main()