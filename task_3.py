array = [4, 2, 5, 1, 3]

for i in range(len(array) - 1):
    for j in range(len(array) - i - 1):
        if array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]

print(array)
