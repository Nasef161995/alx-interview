#!/usr/bin/python3
""" Lockboxes """


def canUnlockAll(boxes):
    """ Method that determines if all the boxes can be opened """
    new_Set = set()
    for i in range(len(boxes)):
        if i == 0:
            boxes[i].sort()
            for j in boxes[i]:
                new_Set.add(j)
        if i in new_Set:
            for j in boxes[i]:
                boxes[i].sort()
                new_Set.add(j)
        else:
            continue
    for i in range(len(boxes)):
        if i in new_Set:
            for j in boxes[i]:
                new_Set.add(j)
        if i == 0:
            continue
        elif i not in new_Set:
            return False
    return True
