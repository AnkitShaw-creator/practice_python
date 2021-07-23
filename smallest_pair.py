for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    if n > 1:
        l.sort()
        print(l[0]+l[1])
    else:
        print(l[0])