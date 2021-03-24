if __name__ == "__main__":
    output = []
    for _ in range(int(input())):
        n = int(input())
        if n%10 == 0:
            output.append(0)
        elif n%5 == 0:
            output.append(1)
        else:
            output.append(-1)

    for i in output:
        print(i)