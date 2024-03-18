#!/usr/bin/python3

"""
You are presented with n locked boxes in a row.
Each box is numbered starting from 0 up to n - 1
and may contain keys to other boxes.
"""


def canUnlockAll(boxes):
    """
    A function to check if all the boxes can be opened.
    :param boxes: List of boxes with keys
    :return: True if all boxes can be opened, False otherwise
    """
    if not boxes or type(boxes) is not list:
        return False

    unlocked = [0]
    for n in unlocked:
        for key in boxes[n]:
            if key not in unlocked and key < len(boxes):
                unlocked.append(key)
    if len(unlocked) == len(boxes):
        return True
    return False
