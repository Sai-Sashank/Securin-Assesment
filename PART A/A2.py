dieA = [1, 2, 3, 4, 5, 6]
dieB = [1, 2, 3, 4, 5, 6]
comb = [[0] * 6 for _ in range(6)]

for i in range(6):
    for j in range(6):
        comb[i][j] = dieA[i] + dieB[j]

for row in comb:
    print(" ".join(map(str, row)))
