import itertools
from math import gcd


def count_sum(a):
    if 0 <= a < 10:
        return a
    else:
        x =[int(b) for b in str(a)]
        return sum(x)


if __name__ == "__main__":
    output = []
    for _ in range(int(input())):
        L, R = map(int, input().split())
        lst = [x for x in range(L, R + 1)]
        l = len([x for x in itertools.combinations(lst, 2) if gcd(count_sum(x[0]), count_sum(x[1])) == 1])
        output.append(l % (pow(10, 9)+7))

    for i in output:
        print(i)