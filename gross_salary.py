for _ in range(int(input())):
    s = int(input())

    if s < 1500:
        gs = s + 0.10*s + 0.90*s
        print(gs)

    if s >= 1500:
        gs = s + 500 + 0.98*s
        print(gs)