d = {"0000": "a", "0001": "b", "0010": "c", "0011": "d", "0100": "e", "0101": "f", "0110": "g", "0111": "h",
     "1000": "i", "1001": "j", "1010": "k", "1011": "l", "1100": "m", "1101": "n", "1110": "o", "1111": "p"}


def decode_str(l):
    ds = ""
    for j in l:
        if j in d.keys():
            ds += d[j]

    return ds


if __name__ == "__main__":
    output = []
    for _ in range(int(input())):
        n = int(input())
        if n % 4 == 0:
            s = input()
            lst = []
            for i in range(0, n, 4):
                lst.append(s[i:i+4])

            output.append(decode_str(lst))

    for i in output:
        print(i)
