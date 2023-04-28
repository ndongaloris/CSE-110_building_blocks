print("\nEnter a list of numbers, type 0 when finished")
numbers = []
number = ''
total_number = 0
while number != 0:
    number = int(input('Enter number:'))
    if number != 0:
        numbers.append(number)
    else:
        break
for number in numbers:
    total_number += number
    average = total_number / len(numbers)

largest_number = max(numbers)
#to understand this function search for list comprehension.
small_positive = min([number for number in numbers if number > 0]) # list comprehension.
print(f'The sum is {total_number} ')
print(f'The average is {average} ')
print(f'The largest number is: {largest_number}')
print(f"The smallest positive number is: {small_positive}")
print("The sorted list is:")
for i, number in enumerate(sorted(numbers)):
   print(number)
