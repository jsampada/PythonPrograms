def recursive(num):
    if num == 1:
        return 1

    return num * (num - 1)


print(recursive(6))