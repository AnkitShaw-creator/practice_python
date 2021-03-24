# to create a series

def create_series(n, k):
    lst = []

    for i in range(n):
        if i < k:
            lst.append(1)
        else:
            sum = 0
            c = k
            for j in reversed(range(i)):
                if c != 0:
                    sum += lst[j]
                    c -= 1
                else:
                    break

            lst.append(sum)
    # print(lst)
    return lst[n-1]


if __name__ == "__main__":
    N, K = map(int, input().split())
    print(create_series(N, K) % 1000000007)

