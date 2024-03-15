#!/usr/bin/python3
boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
opened_box=[]
keys_l = []
def canUnlockAll(boxes):
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

