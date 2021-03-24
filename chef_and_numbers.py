def choose_dishes(n, l):
    d = {}
    i = 0
    while i < n:
        if l[i] == l[i-1] and i != 0:
            l[i] = ' '
        if l[i] in d.keys():
            d[l[i]] += 1
        if l[i] not in d.keys() and l[i] != ' ':
            d[l[i]] = 1
        i+=1

    dish_choice = 1
    for i in d.keys():
        if d[i] > d[dish_choice]:
            dish_choice =i
            continue
        if d[i] == d[dish_choice]:
            dish_choice = min(dish_choice, i)
            continue

    return dish_choice


if __name__ == "__main__":
    output = []
    for _ in range(int(input())):
        N = int(input())
        dishes = list(map(int, input().split()))
        output.append(choose_dishes(N, dishes))

    for i in output:
        print(i)
