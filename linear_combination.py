import itertools
import random
if __name__ == "__main__":
    N = int(input())
    lst = tuple(map(int, input().split()))
    c = 0
    j = 0
    sm = 0
    for i in range(0, 239):
        l = []
        if j<N:
            l.append(i)

