# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# IMPORTS #
from getpass import getpass
from string import ascii_lowercase

# Setup
voyels = ['a', 'e', 'i', 'o', 'u']

# Inputs
pass_phrase = getpass('Pass phrase: ')
PIN = getpass('PIN: ')
CUE = getpass('Cue: ')
pass_phrase = ''.join(pass_phrase.split(' '))  # Removing spaces

# Main 'Cue - Pin - Select algorithm  Credit: https://hal.archives-ouvertes.fr/hal-01781231/document
index = 0  # Pass phrase index
num_sig = 0
output = ''
for (cue_char_index, cue_char) in enumerate(CUE):
    if cue_char in voyels:
        num_sig -= int(PIN[cue_char_index])

    else:
        num_sig += int(PIN[cue_char_index])

    while cue_char not in pass_phrase.lower():
        alphabet_index = ascii_lowercase.index(cue_char)
        new_alphabet_index = (alphabet_index + 1) % 26
        cue_char = ascii_lowercase[new_alphabet_index]

    try:
        index = pass_phrase.lower().index(cue_char, index, len(pass_phrase))

    except ValueError:
        index = pass_phrase.lower().index(cue_char, 0, index)

    index = (index + int(PIN[cue_char_index]) + 1) % len(pass_phrase)
    for _ in range(1, 4):
        output += pass_phrase[index]
        index = (index + 1) % len(pass_phrase)

if num_sig > 0:
    special_char = '!'
elif num_sig < 0:
    special_char = '?'
else:
    special_char = '.'

print(special_char + output + str(abs(num_sig)))
