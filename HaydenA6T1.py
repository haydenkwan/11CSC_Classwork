def inputs():
    global colours
    for i in range(5):
        colour = input('Enter a colour: ')
        colours.append(colour)

def output():
    global colours
    for colour in colours:
        length = len(colour)
        print(f'{colour.title()} {length} characters')

# main
colours = []
inputs()
output()