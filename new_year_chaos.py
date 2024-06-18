def minimumBribes(q):
    b = 0
    i = len(q) - 1

    while i > 0:
        max_ind = i
        c = 1
        for j in range(1, 4):
            if q[max_ind] < q[max_ind - c]:
                max_ind = i - j
                c = 1
            else:
                c += 1
        if i - max_ind > 2:
            print("Too chaotic")
            return
        b += i - max_ind
        q.pop(max_ind)
        i-=1
    print(b)

if __name__ == "__main__":
    minimumBribes([2, 5, 1, 3, 4])