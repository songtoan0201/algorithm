hashset = set()


def isHappy(num):
    sum = 0
    for digit in str(num):
        sum += int(digit)**2
    print(sum)
    if sum != 1 and sum not in hashset:
        hashset.add(sum)
        print("set", hashset)
        return isHappy(sum)

    return sum == 1


print(isHappy(16))
