answer = 0

for i in range(1000, 99, -1):
    for x in range(i, 99, -1):
        prod = i * x

        # Flip the number by acting it's string (basically reverse it)
        if str(prod) == str(prod)[::-1] and answer < prod:
            answer = prod
print(answer)
