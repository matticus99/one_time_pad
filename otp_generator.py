#! /usr/bin/env python3
"""
Generate One Time Pad files, or serve the pads up using a CherryPy server.
"""
import secrets
import uuid


WorkingDir = 'D:\\Code\\Visual Studio Code\\one_time_pad\\pads\\'
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
    """
    Generate a string of random characters, groups in this string are separated by spaces.

    Example:
        NLJDS KW9JG 30AZJ J0XQ4 IRP0Z L6YQT AB7AO RY5XG
    """
    groups = []
    for _ in range(group_count):
        groups.append(''.join([secrets.choice(OTP_CHARS) for _ in range(group_size)]))
    return ' '.join(groups)


def generate_message(row_count=ROW_COUNT, group_count=GROUP_COUNT, group_size=GROUP_SIZE):
    """
    Combine several rows into a single message.
    """
    return '\n'.join(generate_row(group_count, group_size) for _ in range(ROW_COUNT))


"""
Put all messages into the page
"""

messages = (generate_message()+'\n' for _ in range(MESSAGE_COUNT))


with open(WorkingDir + Ident + '_OTP.txt', 'w') as writer:
    for m in messages:
        #print(m)
        writer.write(m)
