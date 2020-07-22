# Example of O(n)


def get_square_numbers(numbers):
    squared_numbers = []
    for number in numbers:
        squared_numbers.append(number * number)
    return squared_numbers


numbers = [1, 2, 3, 4, 5]
squared_numbers = get_square_numbers(numbers)
print(squared_numbers)


# Example of O(n^2)

def Find_Duplicate(arrNum):
    for i in range(len(arrNum)):
        for j in range(i + 1, len(arrNum)):
            if arrNum[i] == arrNum[j]:
                print("{} is duplicate".format(arrNum[i]))
                break


arrNumbers = [1, 2, 4, 9, 55, 2, 'Apple']
print(arrNumbers)
Find_Duplicate(arrNumbers)
