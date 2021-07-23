from math import sqrt

if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())

        if n <= 3:
            print("Yes")
        elif n % 2 == 0 or n % 3 == 0:
            print("No")

        else:
            i = 5
            c = 0
            while i ** 2 <= n:
                if n % i == 0 or n % (i+2) == 0:
                    c += 1
                i += 6
            if c == 0:
                print("Yes")
            else:
                print("No")