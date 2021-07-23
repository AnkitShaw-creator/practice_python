if __name__ == "__main__":
    for _ in range(int(input())):
        N, K = map(int, input().split())
        if N == 0:
            print("0 0")
        elif K == 0:
            print(0, N)
        else:
            print(N // K, N % K)
