numberWords = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine"
}

numbers = [2, 4, 6, 8, 0, 3, 1, 5, 7, 9]

# Now let's translate what is in the numbers list.
for item in numbers:
    print(f'The number {item} is translated as {numberWords.get(item)}.')
