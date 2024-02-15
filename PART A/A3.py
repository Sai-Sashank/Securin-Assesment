dieA = [1, 2, 3, 4, 5, 6]
dieB = [1, 2, 3, 4, 5, 6]
sum_count = [0] * 13
total = len(dieA) * len(dieB)
for i in dieA:
    for j in dieB:
        sum_count[i + j] += 1
for s in range(2, 13):
    count = sum_count[s]
    if count > 0:
        print(f"P (sum = {s}) = {count} / {total}")
