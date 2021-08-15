import math

"""
    1 ≤ T ≤ 20
    1 ≤ N ≤ 100000
"""

def checkPrime(k):
    if k%2 == 0:
        return "No"
    else:
        for i in range(3,int(math.sqrt(k))+1,2):
            if k % i == 0:
                return "No"
    return "Yes"


if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        if 1 < n <= 3:
            print("Yes")
        else:
            print(checkPrime(n))