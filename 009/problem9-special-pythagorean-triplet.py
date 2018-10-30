limit = 1000
for a in range(1, limit + 1):
    for b in range(a + 1, limit + 1):
        hipo = limit - a - b
        if hipo * hipo == a * a + b * b:
            print(a * b * hipo)
            if a + b + hipo == 1000:
                break
