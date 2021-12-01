def generate_primes(limit):
    primes = [True] * limit
    primes[0] = False
    primes[1] = False
    for n, is_prime_number in enumerate(primes):
        if is_prime_number:
            yield n
            for i in range(n * n, limit, n):
                primes[i] = False


def create_primes(limit):
    primes = []
    p = [True] * limit
    p[0] = False
    p[1] = False
    for n, is_prime_number in enumerate(p):
        if is_prime_number:
            primes.append(n)
            for i in range(n * n, limit, n):
                p[i] = False
    return primes


def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    if n == 3:
        return True
    if n % 3 == 0:
        return False
    p = 5
    q = 2
    while n >= p * p:
        if n % p == 0:
            return False;
        p = p + q
        q = 6 - q

    return True


def is_valid(a, b):
    return is_prime(int(str(a) + str(b))) and is_prime(int(str(b) + str(a)))


def example_60():
    primes = create_primes(10000)
    primes.remove(2)
    primes.remove(5)

    for i in range(len(primes)):
        for j in range(len(primes)):
            if j <= i:
                continue
            if is_valid(primes[i], primes[j]):
                for k in range(len(primes)):
                    if k <= j:
                        continue
                    if is_valid(primes[i], primes[k]) and\
                       is_valid(primes[j],primes[k]):
                        for l in range(len(primes)):
                            if l <= k:
                                continue
                            if is_valid(primes[i],primes[l]) and \
                                    is_valid(primes[j], primes[l]) and \
                                    is_valid(primes[k], primes[l]):
                                for m in range(len(primes)):
                                    if m <= l:
                                        continue
                                    if is_valid(primes[i], primes[m]) and \
                                            is_valid(primes[j], primes[m]) and \
                                            is_valid(primes[k], primes[m]) and \
                                            is_valid(primes[l], primes[m]):
                                        print(primes[i], primes[j], primes[k], primes[l], primes[m])
                                        print(primes[i] + primes[j] + primes[k] + primes[l] + primes[m])
                                        return


example_60()
