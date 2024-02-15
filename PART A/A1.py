dieA = [1, 2, 3, 4, 5, 6]
dieB = [1, 2, 3, 4, 5, 6]
total = len(dieA) * len(dieB)
print("Total combinations =", total)
    
for i in dieA:
    for j in dieB:
        print(f"({i}, {j})", end=" ")
    print()
