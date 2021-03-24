
def calculate_fibs(s):
    dict = {}

    for i in s:
        if i not in dict.keys():
            dict[i] =1
        else:
            dict[i] += 1
    # print(dict)

    key_max = max(dict, key=dict.get)

    sum = 0

    l = 2

    for k in sorted(dict, key=dict.get, reverse=True):
        if k != key_max and l > 0:
            sum = sum + dict[k]
            l = l-1

    if len(dict) < 3:
        return "Dynamic"
    if dict[key_max] == sum:
        return "Dynamic"
    else:
        return "Not"


if __name__ == "__main__":
    output = []
    for _ in range(int(input())):
        S = input()

        # calculate_fibs(S)
        output.append(calculate_fibs(S))

    for i in output:
        print(i)
