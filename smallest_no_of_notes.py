if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        notes = 0
        notes += n//100
        n %= 100
        notes += n//50
        n %= 50
        notes += n//10
        n %= 10
        notes += n//5
        n %= 5
        notes += n//2
        n %= 2
        notes += n
        print(notes)