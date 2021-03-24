
def calculate_special_sum(n, k, s, arr):
    count_prime = 0

    for i in arr:
        c = 0
        for j in range(1, i+1):
            if i % j == 0:
                c += 1
        if c <= 2:
            count_prime += 1
    print(sum(arr))
    special_sum = sum(arr) * (k - (count_prime * s))

    return special_sum


if __name__ == "__main__":
    N, K, S = map(int, input().split())
    ARR = list(map(int, input().split()))

    print(calculate_special_sum(N, K, S, ARR))

# WRONG
