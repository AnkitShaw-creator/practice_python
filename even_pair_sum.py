if __name__ == "__main__":
    output = []
    for _ in range(int(input())):
        A, B = map(int, input().split())
        evenA = A // 2
        oddA = A - evenA
        evenB = B // 2
        oddB = B - evenB

        # (X+Y) = evenA+evenB or oddA+oddB
        even_comb = evenA * evenB
        odd_comb = oddA * oddB
        total = even_comb + odd_comb
        output.append(total)

    for i in output:
        print(i)
