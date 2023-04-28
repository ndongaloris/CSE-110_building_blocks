print('\nWelcome to the amusement park!! ')
print()
def access():
    print('Welcome to the ride. Please be safe and have fun!')
def sorry():
    print('Sorry, you may not ride')
age_first_rider = int(input('What is the age of the first rider?: '))
height_first_rider = int(input('What is the height of the first rider?: '))
second_rider = input('Is there a second rider (yes/no)?: ').lower()
if height_first_rider <36:
    sorry()
else:
  if second_rider == 'yes':
      second_rider_age = int(input('What is the age of the second rider?: '))
      second_rider_height = int(input('What is the height of the second rider?: '))
      if second_rider_height >= 36:
          if age_first_rider >= 18 or second_rider_age >= 18:
              access()
          elif age_first_rider in range(12,17) and second_rider_age in range(12,17) and height_first_rider == 52 and second_rider_height == 52:
              access()
          elif (age_first_rider >=16 or second_rider_age >= 16) and (age_first_rider >=14 or second_rider_age >= 14):
            access()
          else:
            sorry()
      else:
        sorry()
  else:         
    if age_first_rider >= 18 and height_first_rider == 62:
        access()
    elif age_first_rider == range(12,17):
      passport = input('Do you have a golden passport?: ')
      if passport == 'yes':
        access()
      else:
        sorry()
    else:
      sorry()

