import random


def subsequences(n, a, l):
    dict = {}
    c = 0
    sm = sum(sorted(l)[:a])
    for _ in range(2**n):
        lt = tuple(random.choices(l, k=a))
        if lt not in dict:
            dict[lt] = sum(lt)

    for i in dict.keys():
        if dict[i] == sm:
            c += 1

    return c


def seq(n, a, l):
    a_seq = []
    c =0
    sm = sum(sorted(l)[:a])
    for _ in range(2 ** n):
        lt = random.choices(l, k=a)
        if lt not in a_seq:
            a_seq.append(lt)

    for i in a_seq:
        if sum(i) == sm:
            print(i)
            c += 1

    return c


if __name__ == "__main__":
    for _ in range(int(input())):
        N, K = map(int, input().split())
        lst = list(map(int, input().split()))
        print(subsequences(N, K, lst))
