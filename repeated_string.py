def repeatedString(s, n):
    c = 0
    for i in range(len(s)):
        if s[i] == 'a':
            c += 1

    c = c * (n // len(s))
    for i in range(n % len(s)):
        if s[i] == 'a':
            c += 1
    
    return c

if __name__ == "__main__":
    print(repeatedString('abcac', 10))