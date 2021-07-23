

if __name__ == "__main__":
    for _ in range(int(input())):
        lst = list(map(int, input().split()))
        c = 0
        c += lst[0]
        if lst[1] == lst[2]:
            c += lst[1]
        elif lst[1] > lst[2]:
            z = lst[1]-lst[2]
            c += lst[2] + (z//3)
        elif lst[1] < lst[2]:
            z = lst[2] - lst[1]
            c += lst[1] + (z//3)

        print(c)