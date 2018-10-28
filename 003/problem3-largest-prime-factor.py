number = 600851475143
prime_factors = list()

for i in range(3, number):
    if number % i == 0:
        prime_factors.append(i)
        number /= i

    if number <= 1:
        break

print(prime_factors)
