import random

num_rows = 5
num_columns = 5
matrix = [[random.randint(0, 9) for i in range(num_rows)] for j in range(num_columns)]

sum_first_diagonal = 0
sum_second_diagonal = 0
sum_first_rows = 0
sum_first_column = 0

[print(x) for x in matrix]

for i in range(num_columns):
    sum_first_diagonal += matrix[i][i]
    sum_second_diagonal += matrix[i][4 - i]
    for j in range(num_columns):
        sum_first_rows += matrix[i][j]
        sum_first_column += matrix[j][i]
    print(f'Сумма столбика №{i+1}: {sum_first_column}')
    print(f'Сумма линии №{i+1}: {sum_first_rows}')
    sum_first_column = 0
    sum_first_rows = 0

print(f'Сумма первой диагонали: {sum_first_diagonal}')
print(f'Сумма второй диагонали: {sum_second_diagonal}')


