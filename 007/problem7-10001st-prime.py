import math
import time


t1 = time.time()


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


count = 1
number = 1
while count < 10001:
    number += 2

    if is_prime_number(number):
        count += 1

        if count == 10001:
            print(number)
