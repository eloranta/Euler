def P3(n):
    return int(n*(n+1)/2) 	# 1, 3, 6, 10, 15, ...


def P4(n):
    return n**2	 	        # 1, 4, 9, 16, 25, ...


def P5(n):
    return int(n*(3*n-1)/2) # 1, 5, 12, 22, 35, ...


def P6(n):
    return n*(2*n-1)	 	# 1, 6, 15, 28, 45, ...


def P7(n):
    return int(n*(5*n-3)/2)	# 1, 7, 18, 34, 55, ...


def P8(n):
    return n*(3*n-2)	 	# 1, 8, 21, 40, 65, .


def gen(func):
    p = []
    n = 1
    while True:
        res = func(n)
        if res > 9999:
            break
        if res > 999:
            p.append((int(res / 100), res % 100))
        n = n+1
    return p


p = [gen(P3), gen(P4), gen(P5), gen(P6), gen(P7), gen(P8)]

for i0 in range(len(p[0])):
    for j1 in range(1, len(p)):
        for i1 in range(len(p[j1])):
            if p[0][i0][1] == p[j1][i1][0]:
                for j2 in range(1, len(p)):
                    if j2 != j1:
                        for i2 in range(len(p[j2])):
                            if p[j1][i1][1] == p[j2][i2][0]:
                                for j3 in range(1, len(p)):
                                    if j3 != j1 and j3 != j2:
                                        for i3 in range(len(p[j3])):
                                            if p[j2][i2][1] == p[j3][i3][0]:
                                                for j4 in range(1, len(p)):
                                                    if j4 != j1 and j4 != j2 and j4 != j3:
                                                        for i4 in range(len(p[j4])):
                                                            if p[j3][i3][1] == p[j4][i4][0]:
                                                                for j5 in range(1, len(p)):
                                                                    if j5 != j1 and j5 != j2 and j5 != j3 and j5 != j4:
                                                                        for i5 in range(len(p[j5])):
                                                                            if p[j4][i4][1] == p[j5][i5][0] and p[j5][i5][1] == p[0][i0][0]:
                                                                                print(p[0][i0], p[j1][i1], p[j2][i2], p[j3][i3], p[j4][i4], p[j5][i5])
                                                                                print(100*p[0][i0][0]+p[0][i0][1] +
                                                                                    100*p[j1][i1][0]+p[j1][i1][1] +
                                                                                    100*p[j2][i2][0]+p[j2][i2][1] +
                                                                                    100*p[j3][i3][0]+p[j3][i3][1] +
                                                                                    100*p[j4][i4][0]+p[j4][i4][1] +
                                                                                    100*p[j5][i5][0]+p[j5][i5][1])



