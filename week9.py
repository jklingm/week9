import os
filename = 'week9'

name = input('What is your name? ')
address = input('What is your address? ')
pnumber = input('What is your phone number? ')

with open(filename, 'w') as file_object:
    file_object.write(f"your name is {name} and you live at {address} and you can be contacted at {pnumber} ")

with open(filename) as file_object:
    for line in file_object:
        print(line)
