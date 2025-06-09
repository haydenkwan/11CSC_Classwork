# Question 4
flag1 = True
flag2 = True
total = 0
num = 1
while flag1:
    try:
        line = int(input('Which length of game is being played(9 or 18): '))
        if line == 9 or line == 18:
            flag1 = False
        else:
            print('Your input must be 9 or 18.')
    except ValueError:
        print('Your input must be a number')
while flag2:
    try:
        for i in range(1, line+1, 1):
            score = int(input(f'What is your score for hole {num}: '))
            if score > 0:
                total = total + score
                num = num + 1
            else:
                print('Your number must be over 0')
                break
        flag2 = False
    except ValueError:
        print('Your input must be a number')
        print('Tally reseting back to 0')
if line == num:
    print(total)
else:
    print('Please run the code again to re-enter your scores')
