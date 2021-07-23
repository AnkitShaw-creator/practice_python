import numpy as np
if __name__ == "__main__":
    n, q = map(int, input().split())
    coins = np.zeros(n, dtype=bool)
    for _ in range(q):
        c, a, b = map(int, input().split())

        if c == 1:
            print(np.count_nonzero(coins[a:b+1]))
        else:
            coins[a:b+1] = ~coins[a:b+1]