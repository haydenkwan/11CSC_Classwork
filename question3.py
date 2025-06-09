# Question 3

name = input('Enter Name: ')
if len(name) < 5:
    newname = name.replace('e', '##')
    newname = newname.replace('i','$')
    newname = newname.replace('E','##')
    newname = newname.replace('I','$')
    print(newname)
else:
    newname = name.replace('o', '###')
    newname = newname.replace('a', '%%')
    newname = newname.replace('O', '###')
    newname = newname.replace('A', '%%')
    print(newname)