vowel = ['a', 'e', 'i', 'o', 'u']
word = "programming"
count = 0
for i in word:
    if i not in vowel:
        count += 1
print(count)

