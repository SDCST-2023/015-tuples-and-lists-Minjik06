#! python3
"""
Ask the user to enter a maximum of 10 positive integers.
After each entry, add the number to a list
If the entry is -1 then stop adding numbers to the list
Sort the list and display the highest number added

inputs:
as many integers as needed

outputs:
Display the largest number:

examples:
Enter an integer:3
Enter an integer:2
Enter an integer:8
Enter an integer:92
Enter an integer:48
Enter an integer:13
Enter an integer:24
Enter an integer:-1

The largest number you entered is 92
"""
ran=[]
for i in range(10):
    intNum=int(input("Enter an integer"))
    ran.append(intNum)
    if intNum>-1:
        continue
    elif intNum<=-1:
        break
ran.sort()
print(ran[-1])

