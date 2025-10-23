def PrimeList(N):
    if N <= 2:
        return ""
    is_prime = [True] * N
    is_prime[0], is_prime[1] = False, False
    for i in range(2, int(N ** 0.5) + 1):
        if is_prime[i]:
            start = i * i
            is_prime[start:N:i] = [False] * len(is_prime[start:N:i])
    primes = [str(num) for num, flag in enumerate(is_prime) if flag]
    return " ".join(primes)