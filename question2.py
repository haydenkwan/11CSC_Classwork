# Question 2

line = input('Enter line: ').upper()
avengers_upper = 'AVENGERS'
if avengers_upper in line:
    new_line = line.replace(avengers_upper, 'BUNNIES')
    print(new_line)
else:
    print('NO BUNNIES FOUND')