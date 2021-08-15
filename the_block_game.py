
def reverse(k):
    s = [x for x in k[::-1]]
    return "".join(map(str, s))


if __name__ == "__main__":
    for _ in range(int(input())):
        n = input()
        if n == reverse(n):
            print("wins")
        else:
            print("loses")