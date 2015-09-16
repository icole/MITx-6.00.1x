def iterPower(base, exp):
    result = 1 if exp == 0 else base
    while exp > 1:
        result *= base
        exp -= 1
    return result

print iterPower(2, 0)
