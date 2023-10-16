def even_number_of_evens(numbers):
    
    if isinstance(numbers, list):
        if numbers == []:
            return False
        else:
            evens = 0

        for n in numbers:
            if n % 2 == 0:
                evens += 1

        if evens:
            return evens % 2 == 0
        else:
            return False
    else:
        raise TypeError("A list was not passed into the function")

if __name__ == '__main__':
    print(even_number_of_evens(5))