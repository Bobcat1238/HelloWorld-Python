print('Greg Barth')
print('o----')
print(' ||||')
print('*' * 10)

numbers = [5, 1010, 2, 5, 2, 777, 2, 8, -2, 99, 3]
largest = numbers[0]
for item in numbers:
    if item > largest:
        largest = item

print(f'The largest number in the list is: {largest}')

tup = (1, 3, 5)
x, y, z = tup
print(tup)
