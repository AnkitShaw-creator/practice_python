if __name__ == "__main__":
    output = []
    for _ in range(int(input())):
        N, K, D = map(int, input().split())
        lst = list(map(int, input().split()))
        sm = sum(lst)
        if sm < K:
            output.append(0)
        if sm >= K:
            d = sm // K
            if d <= D:
                output.append(d)
            else:
                output.append(D)

    for i in output:
        print(i)