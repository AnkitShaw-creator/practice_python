
if __name__ == "__main__":
    for _ in range(int(input())):
        e = [w for w in input()]
        # print(e)
        symbol = []
        l = []

        for i in e:
            if i.isalpha():
                l.append(i)
            elif i == ')':
                l.append(symbol.pop())
            elif i == '(':
                continue
            else:
                symbol.append(i)

        for i in l:
            print(i, end="")
        print()


