def first():
    global square
    print('LIST COMPREHENSION')
    for i in range(1, 11):
        num = i*i
        square.append(num)
    print(square)

def second():
    global square, sum
    print('SUM OF ELEMENTS')
    for num in square:
        sum = sum + num
    print(sum)

def third():
    global list1
    print('REMOVE DUPLICATES')
    line = input('Enter a word: ')
    while line != '':
        line = input('Enter a word: ')
        if line not in list1 and line != '':
            list1.append(line)
    print(list1)       

def fourth():
    global list2, count, word
    print('COUNT OCCURRENCES')
    word.extend(list2)
    for w in word:
        count[w] = count.get(w, 0) + 1
    for word in sorted(count):
        print(word, count[word])

# main
square = []
sum = 0
list1 = []
list2 = ['steak', 'banana', 'chicken', 'banana', 'oven', 'whisk', 'microwave', 'steak', 'oven']
list3 = []
count = {}
word = []
first()
second()
third()
fourth()