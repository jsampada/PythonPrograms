a = [1, 2, 3, 4]
b = [3, 4, 5, 6]

diff_in_a = []
diff_in_b = []

for item in a:
    if item not in b:
        diff_in_a.append(item)

for item in b:
    if item not in a:
        diff_in_b.append(item)

print("Elements in 'a' not in 'b':", diff_in_a)
print("Elements in 'b' not in 'a':", diff_in_b)
