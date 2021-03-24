if __name__ == "__main__":
    output = []
    for _ in range(int(input())):
        lst = list(map(int, input().split()))
        sm = sum(lst)
        if sm == 180:
            output.append("YES")
        else:
            output.append("NO")

    for i in output:
        print(i)