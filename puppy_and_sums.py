
def SUM(D, N):
    sm = 0
    for _ in range(D):
        sm = 0
        for i in range(1, N+1):
            sm = sm+i
        N = sm
    return sm


if __name__ == "__main__":
    output = []
    for _ in range(int(input())):
        d, n = map(int, input().split())
        output.append(SUM(d, n))

    for i in output:
        print(i)