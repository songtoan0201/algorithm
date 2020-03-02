def digitTreeSum(t):
    if not t:
        return 0
    stack = [(t, 0)]
    sum = 0
    while stack:
        cur, v = stack.pop()
        if cur.left or cur.right:
            if cur.left:
                stack.append((cur.left, cur.value + v * 10))
            if cur.right:
                stack.append((cur.right, cur.value + v * 10))
        else:
            sum += cur.value + v * 10
    return sum