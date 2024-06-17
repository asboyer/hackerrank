# problem link https://www.hackerrank.com/challenges/sock-merchant/problem

def sock_merchant(n, ar):
    unmatched = set() # hashset
    pairs = 0 # zero pairs
    for i in range(0, n): # iterate through the array
        if ar[i] in unmatched: # if the element is in the hashset
            unmatched.remove(ar[i]) # remove the element from the hashset
            pairs += 1 # increment the pairs
        else:
            unmatched.add(ar[i]) # add the element to the hashset
    return pairs

if __name__ == '__main__':
    print(sock_merchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20])) # 3