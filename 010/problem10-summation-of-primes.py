import math


def is_prime_number(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    elif n > 2 and n % 2 == 0:
        return False

    max_divisor = math.floor(math.sqrt(n))

    for i in range(3, max_divisor + 1, 2):
        if n % i == 0:
            return False
    return True


limit = 2000000
result = sum((i for i in range(1, limit) if is_prime_number(i)))

print(result)
