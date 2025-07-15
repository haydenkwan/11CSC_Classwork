def first():
  global list1
  print('CREATE A LIST')
  for i in list1:
    print(i)

def second():
  print('FIRST AND LAST ELEMENTS')
  global list2
  print(list2[0])
  print(list2[2])

def third():
  print('LIST LENGTH')
  global list2
  rizz = len(list2)
  print(f'The number of items in this list is {rizz}')

def fourth():
  print('LIST APPEND')
  global list3
  for i in range(1, 6):
    flag = True
    while flag:
      try:
          num = int(input(f'Enter number {i}: '))
          list3.append(num)
          flag = False
      except ValueError:
        print('You must enter a whole number, please try again.')
  print(list3)

def fifth():
  print('SLICING')
  global list4, sublist
  sublist.append(list4[1:4])
  print(sublist)

# main
list1 = ['2', '4', '6', '8', '10']
first()
list2 = ['red', 'green', 'blue']
second()
third()
list3 = []
fourth()
list4 = [10, 20, 30, 40, 50]
sublist = []
fifth()