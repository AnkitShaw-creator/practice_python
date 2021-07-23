if __name__ == "__main__":
    for _ in range(int(input())):
        N, E, H, A, B, C = map(int, input().split())
        if E == H == 0:
            print(-1)
        c = 0
        m = 0
        e = 0