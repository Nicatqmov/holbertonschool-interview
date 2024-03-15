#!/usr/bin/python3
"""
Module for lockboxes.
"""
opened_box=[]
keys_l = []
from typing import List
def canUnlockAll(boxes: List[List[int]]) -> bool:
    """
    Determines if all the boxes can be opened.

    Args:
        boxes (List[List[int]]): A list of lists where each sublist contains the keys inside a box.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """

    if not boxes or len(boxes) == 1:
        return True

    opened_box.append(boxes[0])
    for i in range(100):
        for box in opened_box:
            for keys in box:
                if(keys not in keys_l):
                    keys_l.append(keys)
        for key in keys_l:
            opened_box.append(boxes[key])
    if(0 in keys_l):
        keys_l.remove(0)
    if(len(keys_l) == len(boxes)-1):
        return True
    else:
        return False
    
# Usage example
if __name__ == "__main__":
    boxes = [[1], [2], [3], []]
    print(canUnlockAll(boxes))  # Output: True


