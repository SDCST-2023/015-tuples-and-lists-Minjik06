#!python3
"""
Print the list named "people"
Ask the user to enter a word from the list
Ask the user to enter another word
Replace the first word with the second word.

inputs:
string
string

outputs:
list

example:
['Alain', 'Brian', 'Chris', 'Justin', 'Angela', 'Rick']
Choose a person from the list to replace:Rick
Enter the replacement:Dan
['Alain', 'Brian', 'Chris', 'Justin', 'Angela', 'Dan']

"""
list1=['Alain', 'Brian', 'Chris', 'Justin', 'Angela', 'Rick']
a=str(input("Choose a person from the list to replace: "))
b=str(input("Enter the replacement: "))
for i in range(len(list1)):
    if list1[i]==a:
        list1[i]=b
print(list1)