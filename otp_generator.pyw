#! /usr/bin/env python3

"""
Author: Matt Bernard
otp_generator.py (c) 2021
Desc: One Time pad generator
Created:  2021-02-26T01:29:29.342Z
Modified: !date!
"""

import secrets
import sys
import uuid
import os
import argparse


#File and Path parameters
WorkingDir = os.getcwd()
WorkingFolder = '\\pads\\'
Ident = str(uuid.uuid4().hex)

# Header Message
HEADER = 'Use each set to code your message. After coding the message cut off the set and destroy it.'

parser = argparse.ArgumentParser()

parser.add_argument('-char', type=str, default='ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', 
                   help='The characters available for the One Time Pad')
parser.add_argument('-gs', type=int, default=5, help='The number of characters in each group')
parser.add_argument('-gc', type=int, default=20, help='The groups in each row of a message')
parser.add_argument('-rc', type=int, default=4, help='The number of rows per message')
parser.add_argument('-msg', type=int, default=9, help='The number of messages per page')
parser.add_argument('--screen', help='Print to the screen', action='store_true')

args = parser.parse_args()

# The characters available for the One Time Pad
OTP_CHARS = args.char
# The number of characters in each group, separated by spaces
GROUP_SIZE = args.gs
# The groups in each row of a message, separated by newlines
GROUP_COUNT = args.gc
# The number of rows per message
ROW_COUNT = args.rc
# The number of messages per page
MESSAGE_COUNT = args.msg
# Print to the screen or file?
SCREENOUTPUT = args.screen

def generate_row(group_count=GROUP_COUNT, group_size=GROUP_SIZE):
    # Generate a string of random characters, groups in this string are separated by spaces.

    groups = []
    for _ in range(group_count):
        groups.append(''.join([secrets.choice(OTP_CHARS) for _ in range(group_size)]))
    return ' '.join(groups)


def generate_message(row_count=ROW_COUNT, group_count=GROUP_COUNT, group_size=GROUP_SIZE):
    # Combine several rows into a single message.
    return '\n'.join(generate_row(group_count, group_size) for _ in range(ROW_COUNT))

# Consolidate messages
messages = ('Set ' + str(idx) + '\n' + generate_message()+'\n'*2 for idx in range(MESSAGE_COUNT))

if SCREENOUTPUT:
    for m in messages:
        print(m)
else:
    with open(WorkingDir + WorkingFolder + Ident + '_OTP.txt', 'w') as writer:
        writer.write(HEADER + '\n'*2)
        for m in messages:
            writer.write(m)

