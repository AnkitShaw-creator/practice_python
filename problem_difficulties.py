if __name__ == "__main__":
    for _ in range(int(input())):
        l = list(map(int, input().split()))
        a = set(l)
        if len(a) == 4:
            print(2)
        elif len(a) == 3:
            print(1)
        elif len(a) == 2:
            l.sort()
            x = l[0]
            if l.count(x) == 2:
                print(2)
            else:
                print(1)
        else:
            print(0)