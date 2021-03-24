"""7 8
1 2 2
5
4 8
6 5
2 0 1
1 4"""


def land_count(n, m, s, x, y, xI, yI):
    xI.append(n+1)
    yI.append(m+1)

    land_X = []
    land_Y = []

    #print(xI, yI)
    for i in range(1, x+2):
        val = xI[i]-xI[i-1] -1
        #print(val)
        if val >= s:
            land_X.append(val//s)
    #print("\n")
    for i in range(1, y+2):
        val = yI[i]-yI[i-1] -1
        #print(val)
        if val >= s:
            land_Y.append(val//s)
    #print(land_X, land_Y)
    return sum(land_X) * sum(land_Y)


if __name__ == "__main__":
    output = []
    for _ in range(int(input())):
        N, M = map(int, input().split())  # ROWS, COLUMNS
        X, Y, S = map(int, input().split())
        # NO. OF RIVERS FLOWING HORIZONTALLY, NO. OF RIVERS FLOWING VERTICALLY, DIMENSIONS OF THE HOUSE
        xi = [0]
        yi = [0]
        if X != 0:
            r = input()
            for i in r.split():
                xi.append(int(i))
        if Y != 0:
            g = input()
            for i in g.split():
                yi.append(int(i))

        output.append(land_count(N, M, S, X, Y, xi, yi))
        # print(land_count(N, M, S, X, Y, xi, yi))

    for i in output:
        print(i)