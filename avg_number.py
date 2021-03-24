

def find_num(n, k, v, l):
    sm = (n + k)*v
    p_sum = sum(l)
    s = sm - p_sum
    if s <= 0 or s%k != 0:
        return -1
    else:
        return s//k


if __name__ == "__main__":
    output = []
    for _ in range(int(input())):
        N, K, V = map(int, input().split())
        lst = list(map(int, input().split()))
        output.append(find_num(N, K, V, lst))
    for i in output:
        print(i)