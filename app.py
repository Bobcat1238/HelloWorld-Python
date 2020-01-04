from Utils import FindMax

print('Greg Barth')
print('o----')
print(' ||||')
print('*' * 10)

""" numbers = [5, 1010, 2, 5, 2, 777, 2, 8, -2, 99, 3]
numbers.append(50)
numbers.append(50)
numbers.sort()
largest = numbers[0]
for item in numbers:
    if item > largest:
        largest = item

print(numbers)
numbers.reverse()
print(numbers)
print(f'The largest number in the list is: {largest}')
print(f'The number 50 exists {numbers.count(50)} times in the numbers list.') """

numberList = [5, 1010, 2, 5, 2, 777, 2, 8, -2, 99, 3]
print(numberList)
biggest = Utils.FindMax(numberList)

print()

tup = (1, 3, 5)
x, y, z = tup
print(tup)
