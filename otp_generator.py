#! /usr/bin/env python3

"""
Author: Matt Bernard
otp_generator.py (c) 2021
Desc: One Time pad generator
Created:  2021-02-26T01:29:29.342Z
Modified: !date!
"""

import secrets
import uuid
import os


#File and Path parameters
WorkingDir = os.getcwd()
WorkingFolder = '\\pads\\'
Ident = str(uuid.uuid4().hex)


# The characters available for the One Time Pad
OTP_CHARS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
# The number of characters in each group, separated by spaces
GROUP_SIZE = 5
# The groups in each row of a message, separated by newlines
GROUP_COUNT = 20
# The number of rows per message
ROW_COUNT = 4
# The number of messages per page
MESSAGE_COUNT = 9


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
messages = (generate_message()+'\n' for _ in range(MESSAGE_COUNT))


with open(WorkingDir + WorkingFolder + Ident + '_OTP.txt', 'w') as writer:
    for m in messages:
        writer.write(m)
