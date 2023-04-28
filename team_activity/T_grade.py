print('______________________________________________________________________')
grade =  float(input ('\nwhat is your grade percentage?: '))
print()
A = grade % 10
if grade >= 90: 
  letter = 'A'
elif grade >= 80:
  letter = 'B'
elif grade >= 70:
  letter = 'C'
elif grade >= 60:
  letter = 'D'
else:
  letter = 'F'
if A >=7 and grade < 97 and grade > 59:
    sign = '+'
elif A <3 and grade > 59:
    sign = '-'
else:
    sign =''
print(f'Your letter grade is {letter + sign}')
if grade >=70:
    print('\nCongratulation you have passed!!!, Good luck for the rest. \n')
else:
    print('\nSorry, keep on trying you will surely succeed nextime. \n')
print('_______________________________________________________________________\n')
