def check_lapin(s):
    if len(s) % 2 == 0:
        set1 = [x for x in s[0:len(s)//2]]
        set2 = [x for x in s[len(s)//2:]]

        if sorted(set1) == sorted(set2):
            return "YES"
        else:
            return "NO"
    else:
        set1 = [x for x in s[0:len(s)//2]]
        set2 = [x for x in s[len(s)//2+1:]]

        if sorted(set1) == sorted(set2):
            return "YES"
        else:
            return "NO"


if __name__ == "__main__":
    output = []
    for _ in range(int(input())):
        S = input()
        l = list(S)
        output.append(check_lapin(l))

    for i in output:
        print(i)