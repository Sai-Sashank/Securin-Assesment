def diff_combinations(elements, length):
    if length == 0:
        return [[]]
    total_combinations = []
    for i in range(len(elements)):
        new_elements = elements[:]
        current = elements[i]
        new_elements.remove(current)
        for combo in diff_combinations(new_elements, length - 1):
            total_combinations.append([current] + combo)
    return total_combinations

def probability_sum(arr1, arr2):
    sums = [0] * 12
    for value1 in arr1:
        for value2 in arr2:
            k = value1 + value2
            sums[k - 1] += 1
    sums = [count / 36 for count in sums]
    return sums

def undoom(dieA, dieB):
    a = [1, 2, 2, 3, 3, 4]
    lengthA = 6
    b = [1, 2, 3, 4, 5, 6, 7, 8]
    lengthB = 6
    p_sum_target = [0, 1 / 36.0, 2 / 36.0, 3 / 36.0, 4 / 36.0, 5 / 36.0, 6 / 36.0, 5 / 36.0, 4 / 36.0, 3 / 36.0, 2 / 36.0, 1 / 36.0]
    combos_a = diff_combinations(a, lengthA)
    combos_b = diff_combinations(b, lengthB)
    for combo in combos_a:
        for value in combos_b:
            result = probability_sum(combo, value)
            if result == p_sum_target:
                print("Die A:", combo)
                print("Die B:", value)
                return

dieA = [1, 2, 3, 4, 5, 6]
dieB = [1, 2, 3, 4, 5, 6]
undoom(dieA, dieB)
