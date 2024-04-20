
def longest_common_prefix(words):
    if not words:
        return ""

    # Sort the list of words
    words.sort()
    print(words)

    # Take the first and last words after sorting
    first_word = words[0]
    last_word = words[-1]
    print(first_word)
    print(last_word)

    # Find the common prefix between the first and last words
    prefix = []
    for i in range(len(first_word)):
        if i < len(last_word) and first_word[i] == last_word[i]:
            prefix.append(first_word[i])
        else:
            break

    return "".join(prefix)

# Example usage
words = ["flower", "fljow", "flight","float"]
print(words)
result = longest_common_prefix(words)
print("Output:", result)
