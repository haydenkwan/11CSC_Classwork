# create a list of all the subjects you take at SHC
subjects = ['Math', 'English', 'Physical Science', 'Religious_Education', 'Accounting', 'Physical Education', 'Computer_Science']
# print out each subject in the list
print(subjects)
# get input via keyboard for a new subject and change it to title case and then add to the subject list
new_subject = input('Enter a new subject: ').title()
# sort the subjects in alphabetic order and print out
subjects.append(new_subject)
subjects.sort()
print(subjects)