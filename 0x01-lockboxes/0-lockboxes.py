#!/usr/bin/python3
"""lockboxes """


def canUnlockAll(boxes=[]):
    """
    Returns:
        True if all boxes can be opened, False otherwise.
    """

    if not boxes:
        return False
    keys = set([0])

    for id, box in enumerate(boxes):
        for k in box:
            if k < len(boxes) and k != id:
                keys.add(k)
    if len(keys) != len(boxes):
        return False

    return True
