def is_evenly_divisible(num):
    for i in range(1, 21):
        if num % i != 0:
            return False
    return True


number = 1
while is_evenly_divisible(number) is False:
    number += 1
else:
    print(number)
