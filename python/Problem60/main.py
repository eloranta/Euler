def generate_primes(limit):
    primes = [True] * limit
    primes[0] = False
    primes[1] = False
    for n, is_prime in enumerate(primes):
        if is_prime:
            yield n
            for i in range(n * n, limit, n):
                primes[i] = False


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


def example_60():
    primes = []
    for p in generate_primes(10000):
        primes.append(p)
    primes.remove(2)
    primes.remove(5)

    for i in range(len(primes)):
        for j in range(len(primes)):
            if j <= i:
                continue
            if is_prime(int(str(primes[i]) + str(primes[j]))) and \
                    is_prime(int(str(primes[j]) + str(primes[i]))):
                for k in range(len(primes)):
                    if k <= j:
                        continue
                    if is_prime(int(str(primes[i]) + str(primes[k]))) and \
                            is_prime(int(str(primes[k]) + str(primes[i]))) and \
                            is_prime(int(str(primes[j]) + str(primes[k]))) and \
                            is_prime(int(str(primes[k]) + str(primes[j]))):
                        for l in range(len(primes)):
                            if l <= k:
                                continue
                            if is_prime(int(str(primes[i]) + str(primes[l]))) and \
                                    is_prime(int(str(primes[l]) + str(primes[i]))) and \
                                    is_prime(int(str(primes[j]) + str(primes[l]))) and \
                                    is_prime(int(str(primes[l]) + str(primes[j]))) and \
                                    is_prime(int(str(primes[k]) + str(primes[l]))) and \
                                    is_prime(int(str(primes[l]) + str(primes[k]))):
                                for m in range(len(primes)):
                                    if m <= l:
                                        continue
                                    if is_prime(int(str(primes[i]) + str(primes[m]))) and \
                                            is_prime(int(str(primes[m]) + str(primes[i]))) and \
                                            is_prime(int(str(primes[j]) + str(primes[m]))) and \
                                            is_prime(int(str(primes[m]) + str(primes[j]))) and \
                                            is_prime(int(str(primes[k]) + str(primes[m]))) and \
                                            is_prime(int(str(primes[m]) + str(primes[k]))) and \
                                            is_prime(int(str(primes[l]) + str(primes[m]))) and \
                                            is_prime(int(str(primes[m]) + str(primes[l]))):
                                        print(primes[i], primes[j], primes[k], primes[l], primes[m])
                                        print(primes[i] + primes[j] + primes[k] + primes[l] + primes[m])
                                        return


example_60()
