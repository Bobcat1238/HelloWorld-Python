class Utils:
    #@staticmethod
    def FindMax(self, numbers):
        #numbers = [5, 1010, 2, 5, 2, 777, 2, 8, -2, 99, 3]
        #numbers.append(50)
        #numbers.append(50)
        #numbers.sort()
        largest = numbers[0]
        for item in numbers:
            if item > largest:
                largest = item

        #print(numbers)
        #numbers.reverse()
        print(numbers)
        print(f'The largest number in the list is: {largest}')
        return largest

