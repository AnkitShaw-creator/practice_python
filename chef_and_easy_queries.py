def count_days(limit, queries=[]):
    # wrong process
    c = 0

    n = len(queries)
    i = 0

    while i < n:
        brought_Forward = 0
        if queries[i] > limit:
            brought_Forward = queries[i] - limit
            if i == n - 1:
                n += 1
                queries.append(brought_Forward)
            else:
                next_day_query = queries[i + 1]
                queries.remove(queries.__getitem__(i + 1))
                queries.insert(i + 1, (next_day_query + brought_Forward))

        c += 1
        i += 1
    return c


def easy_queries(limit, queries):
    return (sum(queries) // limit) + 1


if __name__ == "__main__":
    output = []
    for _ in range(int(input())):
        n, k = map(int, input().split())
        lst = list(map(int, input().split()))
        output.append(easy_queries(k, lst))

    for i in output:
        print(i)

