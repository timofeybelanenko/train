with open('u_r_txt_file.txt') as file:
    line = file.readline().replace('\n', '')
    letters = sorted([letter for letter in line])

with open('result.txt', mode='a') as second_file:
    list(map(second_file.write, letters))
