r = range(1, 101)  # range
sum_of_squares = sum((i**2 for i in r))
square_of_sum = sum((i for i in r))**2

result = square_of_sum - sum_of_squares
print(result)
