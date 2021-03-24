import math
if __name__ == "__main__":
    output = []
    for _ in range(int(input())):
        N, D = map(int, input().split())
        lst = list(map(int, input().split()))
        at_risk = [x for x in lst if x < 10 or x > 79]
        not_at_risk =[z for z in lst if 9 < z < 80]
        days = int(math.ceil(len(at_risk) / D)) + int(math.ceil(len(not_at_risk) / D))
        output.append(days)

    for i in output:
        print(i)

