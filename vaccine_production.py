if __name__ == '__main__':

    D1, V1, D2, V2, P = map(int, input().split())
    sm = 0
    i = 1
    while sm < P:
        if i >= D1:
            sm = sm + V1
        if i >= D2:
            sm = sm + V2
        i += 1

    print(i-1)