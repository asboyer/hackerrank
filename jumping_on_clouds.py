def jumpingOnClouds(c):
    path = [0]
    i = 0
    while i < len(c) - 2:
        if c[i + 2] == 0:
            path.append(i + 2)
            i += 2
        elif c[i + 1] == 0:
            path.append(i + 1)
            i += 1
    if i == len(c) - 2:
        if c[i + 1] == 0:
            path.append(i + 1)
            i += 1

    return len(path) - 1

if __name__ == "__main__":
    print(jumpingOnClouds([0, 1, 0, 0, 0, 1, 0])) #3