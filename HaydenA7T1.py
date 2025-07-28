def getWords():
    global words
    word = input('Enter a word: ').upper()
    while word != '':
        if ' ' in word:
            print('You must enter a word (no spaces). Please try again.')
        elif (word not in words) and (' ' not in word) and (word != ''):
            words.append(word) 
        word = input('Enter a word: ').upper()

def printSummary():
    global words
    counter = len(words)
    print(f'You know {counter} unique word(s)!')

# main
words = []
getWords()
printSummary()       