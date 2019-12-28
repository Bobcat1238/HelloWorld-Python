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
print("A translation of our list called numbers using our numberWords dictionary:")
for item in numbers:
    print(f'The number {item} is translated as {numberWords.get(item)}.')

# Now let's translate a phone number the user inputs.
phoneNumber = input("Please enter your phone number: ")
phoneNumeric = int(phoneNumber)
phoneArray = list(phoneNumber)
print(phoneArray)
for digit in phoneNumber:
    print(f' {numberWords.get(int(digit))}')