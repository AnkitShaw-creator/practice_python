import itertools


def count_sequence(n, m, l):
    x = []
    c = 0
    """
    for i in range(1, len(l)+1):
        x.append(list(itertools.combinations(l, i)))
    # print(x)

    for i in x:
        for j in i:
            p = sum(list(j))
            if p > 0 and p % m == 0:
                # print(p)
                c += 1"""

    for i in l:
        if i % m == 0:
            c += 1
    # return c
    return pow(2, c)-1


if __name__ == "__main__":
    output = []
    for _ in range(int(input())):
        N, M = map(int, input().split())
        lst = list(map(int, input().split()))
        output.append(count_sequence(N, M, lst))

    for i in output:
        print(i)

# might be wrong
