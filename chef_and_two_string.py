if __name__ == "__main__":
    output =[]
    for _ in range(int(input())):
        St1 = list(map(str, input()))
        St2 = list(map(str, input()))
        #print(St1)
        #print(St2)
        match = 0
        mis_match = 0
        for i in range(len(St1)):
            if St1[i] != "?" and St2[i] != "?":
                if St1[i] == St2[i]:
                    match += 1
                    #print("{},{}".format(St1[i], St2[i]))
                else:
                    mis_match += 1

        output.append([mis_match, len(St1)-match])

    for i in output:
        print("{} {}".format(i[0], i[1]))