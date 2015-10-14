def count7(N):
    N = str(N)
    if N == "":
        return 0
    else:
        count = 0
        if N[0] == "7":
            count += 1
        count += count7(N[1:])
    return count

print count7(717)
