# Задача 2. Дан файл, содержащий строку с цифрами от 0 до 9. Необходимо отсортировать значения по возрастанию и записать в другой файл.

with open('u_r_txt_file.txt') as file:
    line = file.readline().replace('\n', '')
    letters = sorted([letter for letter in line])

with open('result.txt', mode='a') as second_file:
    list(map(second_file.write, letters))
