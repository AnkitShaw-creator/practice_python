
if __name__ == "__main__":
    output = []
    for _ in range(int(input())):
        N = int(input())
        population = [1, 0, 0]  # [bit, nibble, byte]
        for i in range(0, N):
            if i >= 2:
                bits = population[0]
                population[0] = 0
                population[1] += bits
            if i >= 8:
                nibbles = population[1]
                population[1] = 0
                population[2] += nibbles
            if i >= 16:
                Bytes = population[2]
                population[2] = 0
                population[0] += 2*Bytes

        output.append(population)

    for i in output:
        for j in i:
            print(j, end=' ')



"""
if N<16:
            if N>=2 and N<8:
                bits = population[0]
                population[0]=0
                population[1]=bits
            if N>=8:
                nibbles = population[1]
                population[1]=0
                population[2]=nibbles
        else:
            bits = 2*(N)"""