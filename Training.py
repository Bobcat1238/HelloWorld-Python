#Matrix training
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    for item in row:
        print(item)

#List methods\functions
numbers = [5, 3, 7, 8, 12, 42]
numbers.append(57)
numbers.append(42)
numbers.append(42)
numbers.append(84)
numbers.insert(7,36)
numbers.insert(7,23)
numbers.insert(7,36)
numbers.insert(3,24)
print(numbers)

for number in numbers:
    if (numbers.count(number) > 1):
        print(f'Duplicate number {number} found.')
        print(numbers)
        numbers.remove(number)

print(numbers)