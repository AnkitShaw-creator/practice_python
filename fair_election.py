def swap(a, b):
    return (b, a)


if __name__ == "__main__":
    output = []
    for _ in range(int(input())):
        N, M = map(int, input().split())
        lN = list(map(int, input().split()))  # John Jackson # needs to win
        lM = list(map(int, input().split()))  # Jack Johnson

        c = 0
        n = True
        while n:
            c += 1
            index1 = lN.index(min(lN))  # smallest number index
            index2 = lM.index(max(lM))  # biggest number index
            lN[index1], lM[index2] = map(int, tuple(lM[index2],lN[index1]))
            if sum(lN) > sum(lM):
                n = False

        output.append(c)

    for i in output:
        print(i)
