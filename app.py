print('Greg Barth')
print('o----')
print(' ||||')
print('*' * 10)

numbers = [5, 1010, 2, 5, 2, 777, 2, 8, -2, 99, 3]
largest = 0
largest_has_value = False
for item in numbers:
    if largest_has_value:
        if item > largest:
            largest = item
    else:
        largest = item
        largest_has_value = True

print(f'The largest number in the list is: {largest}')
print("50 is found " + str(numbers.count) + " times in the list.")

tup = (1, 3, 5)
x, y, z = tup
print(tup)
