def getnum():
    flag = True
    while flag:
        try:
            num = int(input('Enter your number: '))
            if num < 0:
                print('Your number must be positive, please try again.')
            else:
                return num
                flag = False
        except ValueError:
            print('Invalid input, please try again.')

def factorial(n):
    for i in range(1, n):
        n = n * i
    return n

def output():
    print(f'The factorial of {number} is {answer}')
 
# main
number = getnum()
answer = factorial(number)
output()