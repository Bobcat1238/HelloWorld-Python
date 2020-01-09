class Utility:
    @staticmethod
    def FindMax(numbers):
        largest = numbers[0]
        for item in numbers:
            if item > largest:
                largest = item

        #print(numbers)
        #numbers.reverse()
        print(numbers)
        print(f'The largest number in the list is: {largest}')
        return largest