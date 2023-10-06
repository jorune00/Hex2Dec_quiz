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



print(generate_random_hex(2))