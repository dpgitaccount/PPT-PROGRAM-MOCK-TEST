def get_even_numbers(input):
    return [num for num in input if num % 2 == 0]

input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
output = get_even_numbers(input)
print(output)

