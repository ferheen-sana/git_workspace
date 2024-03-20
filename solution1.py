def virusindices(p, v):
    indices = []
    for i in range(len(p) - len(v) + 1):
        count_mismatch = 0
        for j in range(len(v)):
            if p[i + j] != v[j]:
                count_mismatch += 1
                if count_mismatch > 1:
                    break
        if count_mismatch <= 1:
            indices.append(str(i))
    if indices:
        print(" ".join(indices))
    else:
        print("No Match!")

# Sample Input 0
test_cases = [
    ("hello", "world"),
    ("banana", "nan")
]

for p, v in test_cases:
    virusindices(p, v)