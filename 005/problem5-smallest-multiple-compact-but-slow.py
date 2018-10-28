is_evenly_divisible = lambda x: all((x % i == 0 for i in range(1, 21)))

number = 1
while is_evenly_divisible(number) is False:
    number += 1
else:
    print(number)
