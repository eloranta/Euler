def p3():
    result = []
    n = 1
    while True:
        p = int(n*(n+1)/2)
        if p > 9999:
            break
        if p > 1010:
            result.append(p)
        n += 1
    return result


def p4():
    result = []
    n = 1
    while True:
        p = n^2
        if p > 9999:
            break
        if p > 1010:
            result.append(p)
        n += 1
    return result


def p5():
    result = []
    n = 1
    while True:
        p = int(n*(3*n-1)/2)
        if p > 9999:
            break
        if p > 1010:
            result.append(p)
        n += 1
    return result


def p6():
    result = []
    n = 1
    while True:
        p = n*(2*n-1)
        if p > 9999:
            break
        if p > 1010:
            result.append(p)
        n += 1
    return result


def p7():
    result = []
    n = 1
    while True:
        p = int(n*(5*n-3)/2)
        if p > 9999:
            break
        if p > 1010:
            result.append(p)
        n += 1
    return result


def p8():
    result = []
    n = 1
    while True:
        p = int(n*(3*n-2))
        if p > 9999:
            break
        if p > 1010:
            result.append(p)
        n += 1
    return result


p = [p3(), p4(), p5(), p6(), p7(), p8()]
print(p)
