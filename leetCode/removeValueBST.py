def deleteFromBST(t, queries):
    for deleteVal in queries:
        t = remove(t, deleteVal)
    return t


def remove(t, deleteVal):
    if t is None:
        return None
    if t.value == deleteVal:
        if t.left:
            t.value = max_of_tree(t.left)
            t.left = remove_rightMost(t.left)
        else:
            t = t.right
    elif deleteVal < t.value and t.left:
        t.left = remove(t.left, deleteVal)
    elif deleteVal > t.value and t.right:
        t.right = remove(t.right, deleteVal)
    return t


def max_of_tree(t):
    if t is None:
        return None
    while t.right:
        t = t.right
    return(t.value)


def remove_rightMost(t):
    if t.right is None:
        return(t.left)
    else:
        t.right = remove_rightMost(t.right)
    return(t)