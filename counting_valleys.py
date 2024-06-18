def countingValleys(steps, path):
    level = 0
    valleys = 0
    for i in range(steps):     
        if path[i] == 'U':
            level += 1
        else:
            level -= 1
        if path[i] == 'U' and level == 0:
            valleys += 1

    return valleys
if __name__ == '__main__':
    steps = 8
    path = 'UDDDUDUU'
    print(countingValleys(steps, path)) # 1