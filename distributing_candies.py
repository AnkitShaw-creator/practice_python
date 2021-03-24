candies = []


def distribute():
    n = len(candies)
    i = 0
    sister = []
    brother = []
    k = 0
    while i < n / 2 and k < n:
        if candies[k] not in sister:
            sister.append(candies[k])
            i += 1
            k += 1

        else:
            k += 1

    return len(sister)


if __name__ == "__main__":
    candies = [1,1]

    print(distribute())
