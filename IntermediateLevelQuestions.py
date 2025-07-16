def first():
    global square
    for i in range(1, 11):
        num = i*i
        square.append(num)
    print(square)

def second():
    global square, sum
    for num in square:
        sum = sum + num
    print(sum)
        
def third():
    global list1, newlist1
    for i in list1:
        if i not in list1:
            newlist1.append(i)
        else:
            break
    print(newlist1)

# main
square = []
sum = 0
list1 = [4, 6, 4, 10, 8, 2, 6]
newlist1 = []
first()
second()
third()