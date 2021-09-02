with open('somefile.txt', 'r') as file:
    with open('sorted_file.txt', mode='w') as second_file:
        second_file.write(''.join(sorted(file.readline())))