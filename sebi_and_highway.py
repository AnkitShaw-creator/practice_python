
def check_guess(s, sg, fg, d, t):
    distance_between_cars = (d*50) / 1000
    time_in_hr = t/3600
    speed = s + (distance_between_cars / time_in_hr)

    # print(speed)

    if abs(speed - sg) < abs(speed - fg):
        return "SEBI"
    else:
        return "FATHER"


if __name__ == "__main__":
    output = []
    for _ in range(int(input())):
        S, SG, FG, D, T = map(int, input().split())
        output.append(check_guess(S, SG, FG, D, T))

    for i in output:
        print(i)