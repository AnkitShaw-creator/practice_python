import io,os,sys

#input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline()
if __name__ == "__main__":
    S = sys.stdin.readline()

    for _ in range(int(sys.stdin.readline())):
        i, j, k, l = map(int, sys.stdin.readline().split())
        s = []
        for c in range(len(S)):
            if c == (i - 1):
                s.append(S[j - 1])
                continue
            if c == (j - 1):
                s.append(S[i - 1])
                continue
            else:
                s.append(S[c])

        st1 = ''.join(s)

        if st1[k - 1] == st1[l - 1]:
            sys.stdout.write("Yes\n")
        else:
            sys.stdout.write("No\n")
