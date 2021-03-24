if __name__ == "__main__":
    output = []
    for _ in range(int(input())):
        X, Y = map(int, input().split())
        c = 0
        while X != Y:
            a = abs(Y-X)
            if a % 2 != 0:
                X = X + a
                c += 1
                continue
            if a % 2 == 0:
                X = X-a
                c += 1
                continue
        output.append(c)

    for i in output:
        print(i)
