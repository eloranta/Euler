def P3():
    result = []
    for n in range(200):
        m = int(n * (n + 1) / 2)
        if 1000 <= m <= 10000:
            result.append(m)
    return result


def P4():
    result = []
    for n in range(100):
        m = n*n
        if 1000 <= m <= 10000:
            result.append(m)
    return result


def P5():
    result = []
    for n in range(100):
        m = n * (3 * n - 1)
        if 1000 <= m <= 10000:
            result.append(m)
    return result


def P6():
    result = []
    for n in range(100):
        m = n * (2 * n - 1)
        if 1000 <= m <= 10000:
            result.append(m)
    return result


def P7():
    result = []
    for n in range(100):
        m = int(n * (5 * n - 3) / 2)
        if 1000 <= m <= 10000:
            result.append(m)
    return result


def P8():
    result = []
    for n in range(100):
        m = n * (3 * n - 2)
        if 1000 <= m <= 10000:
            result.append(m)
    return result


p3 = P3()
p4 = P4()
p5 = P5()
p6 = P6()
p7 = P7()
p8 = P8()

print(p3)
print(p4)
print(p5)
print(p6)
print(p7)
print(p8)

