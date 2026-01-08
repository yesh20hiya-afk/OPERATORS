Amount = int(input('Please enter the amount to be withdrawn: '))

Note_1 = Amount // 100
Note_2 = (Amount % 100) // 50
Note_3 = (Amount % 100 % 50) // 10
print("Number of 100 notes:", Note_1)
print("Number of 50 notes:", Note_2)
print("Number of 10 notes:", Note_3)