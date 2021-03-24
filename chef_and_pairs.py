
def count_pairs(n, l):
    pairs = []
    c =0
    for i in range(0, n):
        for j in reversed(range(n)):
            if l[i] % 2 == 0 and l[j] % 2 != 0 and i<j:
                pairs.append("{}, {}".format(l[i], l[j]))
                c += 1
    # print(pairs)
    return c


if __name__ == "__main__":
    output = []
    for _ in range(int(input())):
        N = int(input())
        lst = list(map(int, input().split()))
        output.append(count_pairs(N, lst))

    for i in output:
        print(i)